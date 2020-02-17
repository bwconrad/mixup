python sample.py \
--dataset cifar10 \
--img_size 32 \
--bottom_width 4 \
--gen_model autogan_cifar10_a \
--latent_dim 128 \
--gf_dim 256 \
--g_spectral_norm False \
--load_path AutoGAN/weights/autogan_cifar10_a.pth \
--exp_name test_autogan_cifar10_a \
--sample_path output/samples \
--num_eval_imgs 100 \