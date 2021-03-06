import torch
import torch.nn as nn
import torch.backends.cudnn as cudnn
import os
import datetime
import random
import numpy as np

from utils import load_config, load_gan, print_and_log
from dataset import load_data
from models import load_model
from train import train, validate

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
cudnn.benchmark = True

# Load config file
config = load_config()

# Set seed
if config['seed']:
    cudnn.benchmark = False
    cudnn.deterministic = True
    np.random.seed(config['seed'])
    torch.manual_seed(config['seed'])
    torch.cuda.manual_seed(config['seed'])
    random.seed(config['seed'])

# Only create output directories and log file if in training mode
if not config['evaluate']:
    # Create directories
    config['output_path'] = "{}{}_{}/".format(config['output_path'], config['arch'], str(datetime.datetime.now().strftime('%Y-%m-%d_%H:%M:%S')))
    if not os.path.exists(config['output_path']):
        os.makedirs(config['output_path'])
    if not os.path.exists(config['data_path']):
        os.makedirs(config['data_path'])

    # Create log file
    config['log'] = config['output_path'] + 'log.txt'
    print_and_log(config, config['log'], printOut=False)

else:
    config['log'] = ''

# Load data
train_loader, test_loader = load_data(config)

# Setup model
net = load_model(config)
net = net.to(device)

# Load GAN generator with pretrained weights
generator = load_gan(config, device)

# Setup optimizer
optimizer = torch.optim.SGD(net.parameters(), lr=config['lr'], momentum=config['momentum'],
                            weight_decay=config['weight_decay'], nesterov=config['nesterov'])

# Setup criterion
criterion = nn.BCEWithLogitsLoss().to(device)

# Resume from checkpoint
if config['resume']:
    if os.path.isfile(config['resume']):
        print_and_log('Loading checkpoint "{}"'.format(config['resume']), config['log'])
        checkpoint = torch.load(config['resume'])
        history = checkpoint['history']
        config['start_epoch'] = checkpoint['epoch']+1
        net.load_state_dict(checkpoint['state_dict'])
        optimizer.load_state_dict(checkpoint['optimizer'])
        print_and_log('Loaded checkpoint "{}" (epoch {})'.format(config['resume'], config['start_epoch']), config['log'])
    else:
        raise FileNotFoundError("Checkpoint file {} does not exist".format(config['resume']))
else:
    history = None
    config['start_epoch'] = 1

# Train or evaluate model
if config['evaluate']:
    assert(config['resume'])
    print('Evaluating checkpoint {} on test set..'.format(config['resume']))
    validate(net, test_loader, criterion, device, config)
else:
    train(net, train_loader, test_loader, optimizer, criterion, generator, history, device, config)
