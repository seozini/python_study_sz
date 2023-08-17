import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
font_path = 'c:\Windows\Fonts\GULIM.TTC'
font_name = font_manager.FontProperties(fname=font_path).get_name()
rc('font0', family = font_name)

vitamins = ['비타민 A', '비타민 B1', '비타민 B2', '비타민 B6', '나이아신', '비타민 C', '비타민 C', '비타민 D', '비타민 E', '엽산' ]
values = [0.18, 0.3, 3.33, 0.38, 3.75, 25, 0.25, 2.75, 0.1]

plt.pie(values, labels=vitamins)
plt.title('시리얼에 포함된 비타민의 함량')
plt.legend(title='비타민 종류', loc='upper left')
plt.axls('equal')

plt.show