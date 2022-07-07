class hparams:

    train_or_test = 'train'
    output_dir = '/content/drive/MyDrive/DLMIA/Colab Notebooks/Pytorch-Medical-Segmentation-master/logs'
    aug = None
    latest_checkpoint_file = 'checkpoint_latest.pt'
    total_epochs = 50
    epochs_per_checkpoint = 1
    batch_size = 1 #Only batch size of 1 works while checking intensities 
    ckpt = '/content/drive/MyDrive/DLMIA/Colab Notebooks/Pytorch-Medical-Segmentation-master/logs/checkpoint_latest.pt'
    # ckpt = None
    init_lr = 0.002
    scheduer_step_size = 20
    scheduer_gamma = 0.8
    debug = False
    mode = '3d' # '2d or '3d'
    in_class = 1
    out_class = 1

    crop_or_pad_size = 512,512,64 # if 2D: 256,256,1
    patch_size = 128,128,32 # if 2D: 128,128,1 ;;; for cti: 5x,5x,x

    # for test
    patch_overlap = 64,64,16 # if 2D: 4,4,0

    fold_arch = '*.mhd'

    save_arch = '.mhd'

    source_train_dir = '/content/drive/MyDrive/DLMIA/data/Challenge data/Training set/Images'
    label_train_dir = '/content/drive/MyDrive/DLMIA/data/Challenge data/Training set/Reference standard'
    source_test_dir = '/content/drive/MyDrive/DLMIA/data/Challenge data/Test set/Images'
    label_test_dir = 'test/label'


    output_dir_test = 'results/your_program_name'