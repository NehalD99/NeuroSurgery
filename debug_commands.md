cv2.imwrite("mask.png",(gt_instances[0].gt_masks.tensor[0].int()*255).cpu().numpy())

cv2.imwrite('test.png',images.tensor[0].permute(1,2,0).cpu().numpy())
