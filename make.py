from jinja2 import Environment, FileSystemLoader, select_autoescape
from poem_parser import parse_poem, parse_date
import os
import glob
import ntpath
import pprint

env = Environment(
    loader=FileSystemLoader(searchpath="./templates/"),
    autoescape=select_autoescape()
)


def parse_content():
    all_volumes = []
    for each_volume in os.listdir('./content/'):
        date = parse_date(open(os.path.join('content', each_volume, 'date.date'), encoding='utf-8').read())
        preface = open(os.path.join('content', each_volume, 'preface.preface'), encoding='utf-8').read()
        content = [date, each_volume, preface]
        poems = []
        for each_content in glob.glob(os.path.join('content', each_volume, '*.txt')):
            data = open(each_content, encoding='utf-8').read()
            parsed_content = parse_poem(data)
            parsed_content.append(
                os.path.join('content', each_volume, ntpath.basename(each_content).split('.')[0] + '_img.png'))
            poems.append(parsed_content)
        content.append(poems)
        all_volumes.append(content)
    all_data = list(sorted(all_volumes, key=lambda x: x[0], reverse=True))
    return all_data


def create_blog_page_html():
    all_volumes = parse_content()
    for index, content in enumerate(all_volumes, 1):
        pprint.pprint(content[-1])
        print('......')
        template = env.get_template("blog_page.html")
        with open(f'{index}.html', 'w', encoding='utf-8') as f:
            f.write(template.render(header=content[1], preface=content[2], content=content[-1]))


if __name__ == '__main__':
    create_blog_page_html()
