import baostock as bs

lg = bs.login()

rs = bs.query_history_k_data_plus("sh.600000",
    "date,code,open,high,low,close,preclose,volume,amount,adjustflag,turn,tradestatus,pctChg,isST",
    start_date='2020-2-07', end_date='2020-2-07',
    frequency="d", adjustflag="3")
print('query_history_k_data_plus respond error_code:'+rs.error_code)
print('query_history_k_data_plus respond  error_msg:'+rs.error_msg)

while (rs.error_code == '0') & rs.next():
    # 获取一条记录，将记录合并在一起
    print(rs.get_row_data())
