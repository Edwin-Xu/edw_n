# coding=utf-8
import os


# 生成目录
def generate_catalogs(path, readme_path, before_text, after_text):
    file_name_list = []
    get_md_list(path, file_name_list)
    write_to_readme(file_name_list, readme_path, before_text, after_text)


def get_md_list(path, file_name_list):
    file_list = os.listdir(path)
    for file_name in file_list:
        # GBK 解码，防止中文乱码问题
        file_name_gbk = file_name
        file_path = os.path.join(path, file_name).replace("\\", "/")
        if os.path.isfile(file_path) and str(file_path).endswith('.md'):
            file_name_list.append(file_path)
        elif not os.path.isfile(file_path):
            get_md_list(file_path, file_name_list)
        else:
            print(file_name_gbk + ' is non-md file, ignored.')

# 写入Readme
def write_to_readme(file_name_list, readme_path, before_text, after_text):
    with open(readme_path, 'w+') as f:
        f.write(before_text.encode('gbk').decode('gbk'))
        for file_name in file_name_list:
            link = '- [%s](%s)\n' % (file_name.replace("./", "").replace("/","-").replace(".md",""), file_name)
            f.write(link.encode('gbk').decode('gbk'))
        f.write(after_text.encode('gbk').decode('gbk'))
    f.close()

if __name__ == '__main__':
    path = './'
    readme_path = './README.md'
    before_text = """
# Edwin Xu个人笔记
> 个人笔记
## 目录
"""
    after_text = """
## 个人说明
- 昵称： Edwin Xu
- [GitHub](https://github.com/Edwin-Xu)
- Email: edwinxu83@gmail.com, 1603837506@qq.com
- [Pages](https://edwin-xu.github.io/)
    """
    generate_catalogs(path, readme_path, before_text, after_text)
