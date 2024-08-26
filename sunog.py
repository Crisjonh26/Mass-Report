#RAPID FB DILDO REPORT V8
#no limit
#CODED BY CRISJHON
#OLD/RP CAN DOWN
#POWERFUL
import requests

def report(cookies, ID_USER, soluong):
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'vi,en-US;q=0.9,en;q=0.8',
        'cache-control': 'max-age=0',
        'dpr': '1',
        'priority': 'u=0, i',
        'sec-ch-prefers-color-scheme': 'light',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
        'sec-ch-ua-full-version-list': '"Not/A)Brand";v="8.0.0.0", "Chromium";v="126.0.6478.127", "Google Chrome";v="126.0.6478.127"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-model': '""',
        'sec-ch-ua-platform': '"Windows"',
        'sec-ch-ua-platform-version': '"10.0.0"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'none',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
        'viewport-width': '811'
    }
    print("SPAM REPORT NUMBER:", soluong)
    home = requests.get(f"https://mbasic.facebook.com/{ID_USER}", cookies=cookies, headers=headers).text
    print("✓ Accessed the account to report")

    next1 = "https://mbasic.facebook.com/rapid_report/?" + home.split("/rapid_report/?")[1].split('"')[0].replace("amp;", "")
    rqnext1 = requests.get(next1, headers=headers, cookies=cookies).text
    print("+ Clicked on the report button")

    next2 = "https://mbasic.facebook.com/frx/basic/select_tag?" + rqnext1.split('action="/frx/basic/select_tag/?')[1].split('"')[0].replace("amp;", "")
    fb_dtsgn2 = rqnext1.split('name="fb_dtsg" value="')[1].split('"')[0]
    jazeostn2 = rqnext1.split('name="jazoest" value="')[1].split('"')[0]
    datanext2 = {
        'fb_dtsg': fb_dtsgn2,
        'jazoest': jazeostn2,
        'tag': 'profile_fake_account',
        'action': 'Submit'
    }
    rqnext2 = requests.post(next2, headers=headers, cookies=cookies, data=datanext2).text
    print("✓ Submitted the fake account report")

    next3 = "https://mbasic.facebook.com/rapid_report/basic/actions/report/confirm/exec?" + rqnext2.split('action="/rapid_report/basic/actions/report/confirm/exec/?')[1].split('"')[0].replace("amp;", "")
    fb_dtsgn3 = rqnext2.split('name="fb_dtsg" value="')[1].split('"')[0]
    jazeostn3 = rqnext2.split('name="jazoest" value="')[1].split('"')[0]
    datanext3 = {
        'fb_dtsg': fb_dtsgn3,
        'jazoest': jazeostn3,
        'checked': 'yes',
        'action': 'Report'
    }
    requests.post(next3, headers=headers, cookies=cookies, data=datanext3)
    print("✓ Confirmed the report")

COOKIE = input("Enter the cookie of the reporting account: ")
acc = input("Enter the ID or username of the account to be reported: ")
sl = int(input("Enter the number of reports: "))
cookie = COOKIE.split(';')
name = []
value = []
for i in range(len(cookie) - 1):
    name.append(cookie[i].split('=')[0].strip())
    value.append(cookie[i].split('=')[1].strip())
cookies = dict(zip(name, value))
for i in range(sl):
    report(cookies, acc, i + 1)