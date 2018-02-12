options = {
    'use_gpu': False,
    'model_path': './bin/mdnet_vot-otb.pth',
    'img_size': 107,
    'padding': 16,
    'batch_pos': 32,
    'batch_neg': 96,
    'batch_neg_cand': 1024,
    'batch_test': 256,
    'n_samples': 256,
    'trans_f': 0.6,
    'scale_f': 1.05,
    'trans_f_expand': 1.5,
    'n_bbreg': 1000,
    'overlap_bbreg': [0.6, 1],
    'scale_bbreg': [1, 2],
    'lr_init': 0.0001,
    'maxiter_init': 30,
    'n_pos_init': 500,
    'n_neg_init': 5000,
    'overlap_pos_init': [0.7, 1],
    'overlap_neg_init': [0, 0.5],
    'lr_update': 0.0002,
    'maxiter_update': 15,
    'n_pos_update': 50,
    'n_neg_update': 200,
    'overlap_pos_update': [0.7, 1],
    'overlap_neg_update': [0, 0.3],
    'success_thr': .01,
    'n_frames_short': 20,
    'n_frames_long': 100,
    'long_interval': 10,
    'w_decay': 0.0005,
    'momentum': 0.9,
    'grad_clip': 10,
    'lr_mult': {'fc6': 10},
    'ft_layers': ['fc'],
}