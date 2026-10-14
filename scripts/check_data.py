from pathlib import Path
import csv
from collections import defaultdict
r=Path(__file__).resolve().parents[1]/'data'
def rows(n): return list(csv.DictReader((r/n).open(encoding='utf-8-sig')))
f=rows('03_每日销售流量.csv');a=rows('04_广告关键词.csv');finance=rows('07_财务事件.csv')
assert round(sum(float(x['净订购销售额美元']) for x in f),2)==254574.30
assert round(sum(float(x['金额美元']) for x in finance),2)==53055.21
assert sum(int(x['订单数']) for x in f)==6743
assert sum(int(x['订购件数']) for x in f)==7522
flow={(x['日期'],x['SKU']):x for x in f}
for x in rows('11_流量来源.csv'):
    y=flow[x['日期'],x['SKU']]
    assert int(x['自然会话数'])+int(x['广告来源会话数'])==int(y['商品会话数'])
    assert int(x['自然订单数'])+int(y['广告归因订单数'])==int(y['订单数'])
agg=defaultdict(lambda:defaultdict(float));cols=['曝光','点击','花费美元','归因订单','归因销售额美元']
for x in rows('13_搜索词明细.csv'):
    for c in cols: agg[x['日期'],x['SKU'],x['关键词']][c]+=float(x[c])
for x in a:
    for c in cols: assert abs(agg[x['日期'],x['SKU'],x['关键词']][c]-float(x[c]))<0.011
for x in rows('08_库存每日.csv'):
    assert int(x['期末可售件数'])==int(x['期初可售件数'])+int(x['补货入库件数'])+int(x['退货入库件数'])-int(x['销售出库件数'])
t=rows('14_月度目标.csv');assert len(t)==54 and len({(x['日期'],x['SKU']) for x in t})==54
print('PASS: sales, profit, orders, units, traffic split, search-term reconciliation, inventory roll-forward and target keys.')
