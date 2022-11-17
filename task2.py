import ants


def main():
    atlasImage = ants.image_read('atlas-T1w.nii.gz', dimension=2)
    givenImage = ants.image_read('given-T1w.nii.gz', dimension=2)
    labelsImage = ants.image_read('atlas-integer-labels.nii', dimension=2)

    # Plot the fixed image
    ants.plot(atlasImage, overlay_cmap="viridis", alpha=0.9, filename='atlasImage.png')
    # Plot the moving image
    ants.plot(givenImage, overlay_cmap="viridis", alpha=0.9, filename='givenImage.png')

    outputPrefix = 'antsR'
    # register give to the space of atlas
    registrationNoMask = ants.registration(fixed=atlasImage, moving=givenImage, 
                            type_of_transform="SyNOnly", regIterations=(100, 75, 20, 0), 
                            verbose=True, outprefix=outputPrefix)
    
    # Plot the fixed and warped moving image
    ants.plot(atlasImage, overlay=registrationNoMask['warpedmovout'], overlay_cmap="viridis", alpha=0.9, filename='fixed_wrap.png')
    
    # Plot the moving and warped fixed image
    ants.plot(givenImage, overlay=registrationNoMask['warpedfixout'], overlay_cmap="viridis", alpha=0.9, filename='moving_wrap.png')
    
    # Trying to binarize the image
    binaryImage = ants.threshold_image(atlasImage)
    ants.plot(binaryImage, overlay_cmap="viridis", alpha=0.9, filename='binaryImage.png')
    
if __name__ == '__main__':
    main()
