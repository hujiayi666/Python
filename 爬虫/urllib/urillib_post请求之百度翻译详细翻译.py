import urllib.request
import urllib.parse
import urllib.response
import json
url="https://fanyi.baidu.com/v2transapi?from=en&to=zh"

header={"Cookie":"BIDUPSID=B6B8169843936E72467EAAD102272EE8; PSTM=1701411144; BAIDUID=B81606E88D5F2DE56575A443F5192CFC:FG=1; BAIDUID_BFESS=B81606E88D5F2DE56575A443F5192CFC:FG=1; ZFY=QcrYfX4KahfqsTiunYwqiEa27nFf0M:B:Bz5LTQ21R2ig:C; __bid_n=18e887e9cab9824db9cc8c; H_PS_PSSID=40302_40375_40366_40459_40482_40514_40398_60043_60023_60035_60048_40511; smallFlowVersion=old; APPGUIDE_10_7_2=1; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; RT=z=1&dm=baidu.com&si=d68c8984-9a32-41c3-818d-f06bd41ab9cc&ss=luv5c69d&sl=c&tt=7jp&bcn=https%3A%2F%2Ffclog.baidu.com%2Flog%2Fweirwood%3Ftype%3Dperf&ld=qib7&ul=3gqaq&hd=3gqbx; BA_HECTOR=85agal2l84a184a021040h0kg2o3ok1j1kls21t; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; PSINO=3; delPer=0; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1712834660,1713002380; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1713002514; ab_sr=1.0.1_ZTA2M2VhOGQxNjMxYzU1YmJhZWZjYjM5NzQzZjIwZTBlNGM5ZTMwZmQ3YmVhOWRmZTc4ZDEwYzBjNGUxMTA4ZTlhZmE2ODFhMjQ1MTliY2NiNmEyNTMxYzI1ZmI2Y2QxYzUzZWE4YTM5ZWQzZjEzNjAxMDkxYmVlMjRmZjk0NTMyYzhiMGIyZDBjMWViNGUzMDhiMmRjMDRjZDYzN2QwNg=="}
data={
"from":"en",
"to":"zh",
"query":"love",
"simple_means_flag":"3",
"sign":"198772.518981",
"token":"96533f59e1ff0df5e832f3511a63475a",
"domain":"common"}

#post请求的参数必须编码
data=urllib.parse.urlencode(data).encode("UTF-8")
#post的请求的参赛，是不会拼接在url的后面的，而是需要放在请求对象定制的参数中
#post请求的参数，必须编码
request=urllib.request.Request(url=url,data=data,headers=header)
#模拟浏览器向服务器发送请求
response=urllib.request.urlopen(request)
#获取响应数据
content=response.read().decode("UTF-8")
obj=json.loads(content)
print(obj)












