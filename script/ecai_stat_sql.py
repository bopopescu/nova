#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ecai统计数据
sql_ecai_stat1 = """SELECT a.organizationId,b.organizationName,a.customerId,a.customerName,a.accountingUserCode,a.accountSetId,a.inputTime as createCustomerTime,c.inputTime as createAccountTime
FROM taxagency_customer a
LEFT JOIN taxagency_customer_accountinfo c on a.customerId=c.customerId
LEFT JOIN taxagency_organization b on a.organizationId=b.organizationId
where a.customerState='00' and a.organizationId=b.organizationId and a.customerName NOT LIKE %s
and a.customerName NOT LIKE %s and a.customerName NOT LIKE %s and a.customerName NOT LIKE %s
and a.customerName NOT LIKE %s and a.customerName NOT LIKE %s and a.customerName NOT LIKE %s
and a.customerName NOT LIKE %s and a.customerName NOT LIKE %s AND a.customerName NOT LIKE %s
and a.customerId not in ('cus17900000018019','cus17900000059013','cus17900000059017','cus17900000113211',
'cus17900000018010','cus17900000022008','cus17900000022007','cus17900000039006','cus17900000057015','cus17900000057016',
'cus17900000064007','cus17900000064263','cus17900000063269','cus17900000065247','cus17900000065252','cus17900000080068',
'cus17900000080069','cus17900000082056','cus17900000081040','cus17900000081039','cus17900000093023','cus17900000096003',
'cus17900000100017','cus17900000106122','cus17900000113112','cus17900000113149','cus17900000112145','cus17900000112179',
'cus18900000122166','cus18900000132024','cus18900000127276','cus18900000126089')
and a.accountingUserCode not IN
('YH15900000042607','YH17900000378071','YH17900000378072','YH17900000380146','YH17900000380148','YH17900000388167',
'YH17900000385911','YH17900000393434','YH17900000394004','YH17900000420214','YH15900000080050','YH17900000383253',
'YH17900000399420','YH17900000420361','YH15900000068565','YH16900000283814','YH16900000320581','YH16900000371030',
'YH17900000377759','YH17900000386955','YH17900000387018','YH17900000418291','YH17900000385908','LSYC0000001151',
'000000000122','YH15900000171665','YH16900000277002','YH16900000291211','YH17900000380159','YH17900000373832',
'YH16900000371050','YH16900000280906','YH16900000369989','YH16900000262581','YH17900000374039','YH16900000277004',
'YH17900000375120','YH15900000049199','YH15900000042282','YH17900000384213','YH17900000374040','YH17900000411505',
'YH16900000349647','YH15900000025001','YH16900000331186','YH17900000419398','LSYC0000001150','YH17900000379408',
'YH17900000381423','000000000005','LSYC0000000762','YH15900000056032','YH15900000129341','YH16900000367132','YH17900000380125')
GROUP BY a.organizationId,a.customerId
ORDER BY a.inputTime ASC""".encode('utf-8')

# 柠檬云库获取某账套最早新增凭证时间
sql_ecai_stat2 = "SELECT TOP 1 CREATED_DATE FROM ACC_VOUCHER where AS_ID=%s ORDER BY CREATED_DATE ASC"

# 柠檬云库获取某账套最后动账时间
sql_ecai_stat3 = "SELECT TOP 1 MODIFIED_DATE FROM ACC_VOUCHER where AS_ID=%s ORDER BY MODIFIED_DATE DESC"

sql_ecai_stat4 = "SELECT inputFirstVouTime, updateLastVouTime FROM stat_customer_detail where accountSetId=%s"