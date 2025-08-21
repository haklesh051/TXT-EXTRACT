import datetime

def create_html_file(file_name, batch_name, contents):
    tbody = ''
    for line in contents:
        if ':' not in line:  # agar colon hi nahi hai to skip karo
            print("⚠️ Skipping invalid line:", line)
            continue
        try:
            text, url = [item.strip('\n').strip() for item in line.split(':', 1)]
            tbody += f'<tr><td><a href="{url}">{text}</a></td></tr>'
        except Exception as e:
            print("⚠️ Error in line:", line, e)
            continue

    with open('template.html') as fp:
        file_content = fp.read()

    with open(file_name, 'w') as fp:
        fp.write(file_content.replace('tbody_content', tbody).replace('batch_name', batch_name))
