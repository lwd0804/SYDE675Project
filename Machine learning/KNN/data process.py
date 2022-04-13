import os

train_txt_path = '/Users/mac/Downloads/train.txt'
train_dir = '/Users/mac/Downloads/seg_train/'
test_txt_path = '/Users/mac/Downloads/test.txt'
test_dir = '/Users/mac/Downloads/seg_test/'
label_class = ['buildings', 'forest', 'glacier', 'mountain', 'sea', 'street',
               ]
def gen_txt(txt_path, img_dir):
    f = open(txt_path, 'w')
    for root, s_dirs, _ in os.walk(img_dir, topdown=True):
        for sub_dir in s_dirs:
            print(s_dirs)
            i_dir = os.path.join(root, sub_dir)
            img_list = os.listdir(i_dir)
            print(root)
            newdir=os.path.join('/content/train/',sub_dir)
            # newdir = os.path.join('/content/test/', sub_dir)
            for i in range(len(img_list)):
                label=sub_dir
                # img_path = os.path.join(i_dir, img_list[i])
                img_path = newdir + '/' + img_list[i]
                label = label_class.index(label)
                line = img_path + ' '+str(label) + '\n'
                f.write(line)
    f.close()


gen_txt(train_txt_path, train_dir)
# gen_txt(test_txt_path, test_dir)
