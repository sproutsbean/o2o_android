import sys
import time
from com.ea.common import tools
from com.ea.common import web_login

logger = tools.create_logger()


def caiwu_approve(webdriver, loanno, screenshot_path):
    u"""财务审批"""
    casename = sys._getframe().f_code.co_name
    view = "OK"
    except_result = "流程结束"
    process_type = "平台财务"
    # self.loanno = "SK0027-BK-1712-00009"
    logger.info("财务审批开始")
    logger.info("使用的贷款单号是:" + loanno)
    from com.ea.pages.approve_page import TodoPage, ApproveCaiwuPage
    from com.ea.common import web_menu
    try:
        current_approver, node_name = tools.get_approver_acount_by_yewuno(loanno, process_type)
        if not current_approver:
            raise Exception
        web_login.login(webdriver, username=current_approver)
        todopage = TodoPage(webdriver)
        approvecaiwupage = ApproveCaiwuPage(webdriver)
        # 进入待办查询页面
        web_menu.go_to_wait_todo_query(webdriver)
        todopage.input_yewuno(loanno)
        # todopage.click_query_all()
        todopage.click_search_button()
        todopage.click_first_row(process_type)
        # 拖动页面到最下面
        approvecaiwupage.scroll_to_special_condition()
        approvecaiwupage.input_special_condition(view)
        approvecaiwupage.click_save_button()
        approvecaiwupage.click_confirm_button()
        approvecaiwupage.input_approve_view(view)
        approvecaiwupage.click_tongguo_button()
        approvecaiwupage.click_confirm_button()
        time.sleep(3)
        # web_menu.go_to_platform_caiwu_approve(webdriver)
        # actual_result = approvecaiwupage.get_result(loanno)
        assert "暂无数据" in webdriver.page_source
        logger.info("财务审批结束")
    except Exception as e:
        tools.screenshot(webdriver, screenshot_path, casename)
        raise e
