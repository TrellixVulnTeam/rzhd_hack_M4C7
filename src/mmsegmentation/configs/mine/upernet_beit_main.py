_base_ = [
    'upernet_beit.py', 'raildata_convnext.py',
    'default_runtime.py', 'schedule_160k.py'
]

checkpoint_file = 'https://download.openmmlab.com/mmsegmentation/v0.5/beit/upernet_beit-base_8x2_640x640_160k_ade20k/upernet_beit-base_8x2_640x640_160k_ade20k-eead221d.pth'  # noqa
model = dict(
    # pretrained='pretrain/beit_base_patch16_224_pt22k_ft22k.pth',
    init_cfg=dict(
            type='Pretrained', checkpoint=checkpoint_file),
    test_cfg=dict(mode='slide', crop_size=(640, 640), stride=(426, 426)))

optimizer = dict(
    _delete_=True,
    type='AdamW',
    lr=3e-5,
    betas=(0.9, 0.999),
    weight_decay=0.05,
    constructor='LayerDecayOptimizerConstructor',
    paramwise_cfg=dict(num_layers=12, layer_decay_rate=0.9))

lr_config = dict(
    _delete_=True,
    policy='poly',
    warmup='linear',
    warmup_iters=1500,
    warmup_ratio=1e-6,
    power=1.0,
    min_lr=0.0,
    by_epoch=False)

# By default, models are trained on 8 GPUs with 2 images per GPU
data = dict(samples_per_gpu=2)
