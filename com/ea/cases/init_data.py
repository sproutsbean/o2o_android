#!usr/bin/env python
# -*- coding:utf-8 -*-


# 初始化数据

# 待办查询
wf_process_task_main = "INSERT INTO `wf_process_task_main` (`task_id`, `task_code`, `process_id`, `process_name`, `process_type`, `system_module`, `process_version`, `refer_id`, `refer_url`, `refer_code`, `appliedby`, `appliedby_name`, `applied_date`, `is_system_start`, `auditor_stime`, `auditor_etime`, `process_status`, `auditor_steps`, `auditor_crr_step`, `cur_node_id`, `cur_node_stime`, `org_id`, `org_name`, `applied_des`, `remark`, `time_effective`, `used_time`, `overtime`) VALUES	('autotestlnsud59rne38i', 'autotest_REQ_PDR-SZ-1707-00039', 'autotestldmiv6pj0id8i', '需求申请', 'REQUIREMENT_APP', 'O2O', NULL, 'autotestlnrg2v5pgj2ik', 'http://service.o2osit.eascs.com/demand/approval?1=1&mainapplyNo=lnrg2v5pgj2ik', 'autotest_PDR-SZ-1707-00039', '184118', '申请人：陈玮-金融', '2017-07-25 11:19:45', 0, '2017-07-25 11:19:45', NULL, 2, 6, 4, 'autotestlnsuerta53opf', '2017-07-25 14:40:35', '23796', '江苏锦润', '需求申请：关于广西客户李德明结清后，退回多支付的款项需修改数据的申请', NULL, 0, 0, 0),	('autotestm2lp7al49fkbk', 'autotest_REQ_PDR-1806-00014', 'autotestldmiv6pj0id8i', '需求申请', 'REQUIREMENT_APP', 'O2O', NULL, 'autotestm2lohce7p25if', 'http://service.o2osit.eascs.com/demand/approval?1=1&mainapplyNo=m2lohce7p25if', 'autotest_PDR-1806-00014', '161332', '申请人：胡珊-O2O金融', '2018-06-22 10:36:26', 0, '2018-06-22 10:36:26', NULL, 2, 6, 4, 'autotestm2lp9afpplm3p', '2018-06-22 10:53:29', '1', '总部', '需求申请：系统代偿金额与银行实际扣款不一致', NULL, 0, 134.4, 134.4),	('autotestm3qmpapfgqm2t', 'autotest_REQ_PDR-1806-00055', 'autotestldmiv6pj0id8i', '需求申请', 'REQUIREMENT_APP', 'O2O', NULL, 'autotestm3qltga5gurlb', 'http://service.o2osit.eascs.com/demand/approval?1=1&mainapplyNo=m3qltga5gurlb', 'autotest_PDR-1806-00055', '181229', '申请人：黎亮君', '2018-06-25 14:31:00', 0, '2018-06-25 14:31:00', NULL, 2, 6, 4, 'autotestm3qmqsd4no8s5', '2018-06-25 17:21:43', '9', '广西', '需求申请：莫香玉虚退保证金转代偿回款', NULL, 0, 123.483, 123.483),	('autotestm82nk0hc3eqst', 'autotest_REQ_PDR-1807-00169', 'autotestldmiv6pj0id8i', '需求申请', 'REQUIREMENT_APP', 'O2O', NULL, 'autotestm82k9ijp5uiuq', 'http://service.o2osit.eascs.com/demand/approval?1=1&mainapplyNo=m82k9ijp5uiuq', 'autotest_PDR-1807-00169', '202025', '申请人：王荣非', '2018-07-12 19:04:02', 0, '2018-07-12 19:04:02', NULL, 2, 6, 4, 'autotestm82nll93ao3o9', '2018-07-13 08:59:14', '13', '河南', '需求申请：单号：HEN050-BP-1806-00001，借款人：苏万生，进件渠道由：旺旺漯河办事处改为：伊川县华久副食批发部部', NULL, 0, 16, 16),	('autotestm9la6em5hh7s1', 'autotest_REQ_PDR-1807-00173', 'autotestldmiv6pj0id8i', '需求申请', 'REQUIREMENT_APP', 'O2O', NULL, 'autotestm9l8o5dq5scgh', 'http://service.o2osit.eascs.com/demand/approval?1=1&mainapplyNo=m9l8o5dq5scgh', 'autotest_PDR-1807-00173', '239164', '申请人：陈晓君-金融', '2018-07-13 09:56:34', 0, '2018-07-13 09:56:34', NULL, 2, 6, 4, 'autotestm9la6asc4gso2', '2018-07-13 10:00:03', '1', '总部', '需求申请：需要修改--高利率单据', NULL, 0, 15.0667, 15.0667);"