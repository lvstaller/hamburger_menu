def inf(model=None, img=None):

    results = model(img)  # batched inference

    res = results.crop(save=False)
    
    if len(res) > 0:
        box = res[0]["box"]
        img = img[
        int(box[1]) : int(box[3]),
        int(box[0]) : int(box[2]),]
        return img
    else:
        return [None, None]
    # 


    # results.print()  # or .show(), .save(), .crop(), .pandas(), etc.
