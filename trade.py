#########################################
################ 策略1 ##################
#########################################
估价高于20日均线买，低于20日均线卖
import tushare as ts
import matplotlib.pyplot as plt

def parse(STOCK):
	is_buy = 0
	buy_val = []
	buy_date=[]
	sell_val=[]
	sell_date=[]
	df = ts.get_hist_data(STOCK)
	ma20=df['ma20']
	close=df['close']
	rate=1.0
	rate_list=[]
	idx=len(ma20)

	while idx > 0:
		idx -= 1
		close_val = close[idx]
		ma20_val = ma20[idx]
		if close_val > ma20_val:
			if is_buy == 0:
				is_buy = 1
				buy_val.append(close_val)
				buy_date.append(close.keys()[idx])
		elif close_val < ma20_val:
			if is_buy == 1:
				is_buy=0
				sell_val.append(close_val)
				sell_date.append(close.keys()[idx])
				rate=rate*(sell_val[-1]*(1-0.002)/buy_val[-1])
				rate_list.append(rate)
				continue
		rate_list.append(rate)
	
	print  "stock number: %s" %STOCK
	print "buy count: %d" %len(buy_val)
	print "sell count: %d" %len(sell_val)

#	rate_list=[1]
	for i in range(len(sell_val)):
#		rate=rate*(sell_val[i]*(1-0.002)/buy_val[i])
#		rate_list.append(rate)
		print "buy date: %s, buy price: %.2f" %(buy_date[i], buy_val[i])
		print "sell date: %s, sell price: %.2f" %(sell_date[i], sell_val[i])
	print "rate: %.2f" % rate_list[-1]
#	print rate_list

	x_axis=range(1, len(ma20)+1)
	label=list(df.index)[::-1]
	plt.plot(x_axis, rate_list)
	plt.show()
	

if __name__=='__main__':
	STOCK='600000'
	parse(STOCK)
