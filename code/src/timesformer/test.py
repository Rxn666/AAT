import torch
check = torch.load('/home/yqx/yqx_softlink/VAPT_code/src/timesformer/mae_supervisied_checkpoint_new.pth')
print(check['model'].keys())
# print(check['model']['blocks.37.attn.qkv.weight'].shape)
# k = 'blocks.37.attn.qkv.weight'
# spk = k.split('.')
# print(spk[0:2])