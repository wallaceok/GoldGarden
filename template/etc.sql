/*--------------------etc卡流水------------------------------------------------------------------*/
SELECT * FROM etc_entrust_detail ORDER BY created_time DESC
SELECT COUNT(*)   FROM etc_entrust_detail


UPDATE  etc_entrust_detail SET op_time = '2017-11-16 15:00:04' WHERE id = '923'

SELECT card_no AS '卡号',in_op_time AS '进站时间', out_op_time AS '出站时间', etc_money AS '实扣金额' ,statis_date AS '记账时间' ,op_time AS '收费时间',DELETED AS '数据是否被删除'
FROM  etc_entrust_detail WHERE id = '923'


