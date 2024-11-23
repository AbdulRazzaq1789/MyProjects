import os
import platform
import subprocess

def open_file(file_path):
    try:
        if platform.system() == "Windows":
            os.startfile(file_path)  # For Windows
        elif platform.system() == "Darwin":  # macOS
            subprocess.run(["open", file_path])
        else:  # For Linux
            subprocess.run(["xdg-open", file_path])
        print(f"Opened: {file_path}")
    except Exception as e:
        print(f"Failed to open {file_path}: {e}")

def get_site_name():
    site_name = input('Please Enter the Site Name: ')
    site_id = ''
    try:
        for digit in reversed(site_name):
            if digit.isdigit():
                site_id += digit

            else:
                break
    except Exception as e:
        print(e)

    return "".join(reversed(site_id))


def get_site_ip():
    SITES = {
        1:  'گل سرخ',
        2:  'بهارستان',
        3: 'زمان خان',
        4:  'تپه وزیر اکبر خان',
        5: ' برچی',
        6: ' کوتل',
        7: 'پروان ',
        8: ' ده افغانان',
        9: 'ارزان قیمت ',
        11: 'باغ بالا ',
        12: 'کوته سنگی مربوط HKB',
        13: 'کارته نو',
        14: 'کوته سنگی',
        15: 'دارالامان',
        16: 'دفتر مرکزی ویسترن',
    }
    site_name = get_site_name()
    base_id = None
    qrt_id = None
    med = len(site_name)//2
    base_id = int(site_name[:med])
    qrt_id = int(site_name[med:])

    file_name = 'site-name.txt'

    with open(file_name, 'w') as file:
        file.write(f"Site IP: 10.150.{base_id}.{qrt_id}\nBase Name: {SITES.get(base_id)}")

    open_file(file_name)

get_site_ip()

    
    







