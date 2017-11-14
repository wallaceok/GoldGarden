#!/usr/bin/python3
# coding:utf-8
from __future__ import print_function
import datetime
import io
import sys
import unittest
from xml.sax import saxutils


class OutputRedirector(object):
    def __init__(self, fp):
        self.fp = fp

    def write(self, s):
        self.fp.write(s)

    def writelines(self, lines):
        self.fp.writelines(lines)

    def flush(self):
        self.fp.flush()

stdout_redirector = OutputRedirector(sys.stdout)
stderr_redirector = OutputRedirector(sys.stderr)


class TemplateMixin(object):

    STATUS = {0: '通过', 1: '失败', 2: '错误', }

    DEFAULT_TITLE = 'Unit Test Report'
    DEFAULT_DESCRIPTION = ''

    # ----------------------- HTML板-------------------------------------------------

    html_template = r"""<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <title>%(title)s</title>
    <meta name="generator" content="%(generator)s"/>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8"/>
    %(stylesheet)s
</head>
<body>
<script language="javascript" type="text/javascript"><!--
output_list = Array();

/* level - 0:Summary; 1:Failed; 2:All */
function showCase(level) {
    trs = document.getElementsByTagName("tr");
    for (var i = 0; i < trs.length; i++) {
        tr = trs[i];
        id = tr.id;
        if (id.substr(0,2) == 'ft') {
            if (level < 1) {
                tr.className = 'hiddenRow';
            }
            else {
                tr.className = '';
            }
        }
        if (id.substr(0,2) == 'pt') {
            if (level > 1) {
                tr.className = '';
            }
            else {
                tr.className = 'hiddenRow';
            }
        }
    }
}


function showClassDetail(cid, count) {
    var id_list = Array(count);
    var toHide = 1;
    for (var i = 0; i < count; i++) {
        tid0 = 't' + cid.substr(1) + '.' + (i+1);
        tid = 'f' + tid0;
        tr = document.getElementById(tid);
        if (!tr) {
            tid = 'p' + tid0;
            tr = document.getElementById(tid);
        }
        id_list[i] = tid;
        if (tr.className) {
            toHide = 0;
        }
    }
    for (var i = 0; i < count; i++) {
        tid = id_list[i];
        if (toHide) {
            document.getElementById('div_'+tid).style.display = 'none'
            document.getElementById(tid).className = 'hiddenRow';
        }
        else {
            document.getElementById(tid).className = '';
        }
    }
}


function showTestDetail(div_id){
    var details_div = document.getElementById(div_id)
    var displayState = details_div.style.display
    // alert(displayState)
    if (displayState != 'block' ) {
        displayState = 'block'
        details_div.style.display = 'block'
    }
    else {
        details_div.style.display = 'none'
    }
}


function html_escape(s) {
    s = s.replace(/&/g,'&amp;');
    s = s.replace(/</g,'&lt;');
    s = s.replace(/>/g,'&gt;');
    return s;
}

/* obsoleted by detail in <div>
function showOutput(id, name) {
    var w = window.open("", //url
                    name,
                    "resizable,scrollbars,status,width=800,height=450");
    d = w.document;
    d.write("<pre>");
    d.write(html_escape(output_list[id]));
    d.write("\n");
    d.write("<a href='javascript:window.close()'>close</a>\n");
    d.write("</pre>\n");
    d.close();
}
*/
--></script>

%(heading)s
%(report)s
%(ending)s

</body>
</html>
"""
    # 变量: (title, generator, stylesheet, heading, report, ending)

    # ------------------------------------------------------------------------
    # Stylesheet[样式表]
    #
    # 也可以使用外部样式表的作用例如.
    #   <link rel="stylesheet" href="$url" type="text/css">

    STYLESHEET_TMPL = """
<style type="text/css" media="screen">
body        { font-family: verdana, arial, helvetica, sans-serif; font-size: 80%; }
table       { font-size: 100%; }
pre         { }

/* -- heading ---------------------------------------------------------------------- */
<!--h1 {font-size: 16pt;color: gray;}
.heading {
    margin-top: 0ex;
    margin-bottom: 1ex;
}

.heading .attribute {
    margin-top: 1ex;
    margin-bottom: 0;
    font-family:"华文行楷";
}

.heading .description {
    margin-top: 4ex;
    margin-bottom: 6ex;
}-->

/* -- css div popup ------------------------------------------------------------------------ */
a.popup_link {
}

a.popup_link:hover {
    color: red;
}

.popup_window {
    display: none;
    position: relative;
    left: 0px;
    top: 0px;
    /*border: solid #627173 1px; */
    padding: 10px;
    background-color: #E6E6D6;
    font-family: "Lucida Console", "Courier New", Courier, monospace;
    text-align: left;
    font-size: 8pt;
    width: 500px;
}

}
/* -- report ------------------------------------------------------------------------ */
<!--#show_detail_line {
    margin-top: 3ex;
    margin-bottom: 1ex;
}-->
#result_table {
    width: 80%;
    border-collapse: collapse;
    border: 1px solid #777;
}
<!--#header_row {
    font-weight: bold;
    color: white;
    background-color: #777;
}-->
#result_table td {
    border: 1px solid #777;
    padding: 2px;
}
<!--#total_row  { font-weight: bold; }-->
<!--
.passClass  { background-color: #6c6; }
.failClass  { background-color: #c60; }
.errorClass { background-color: #c00; }
.passCase   { color: #6c6; }
.failCase   { color: #c60; font-weight: bold; }
.errorCase  { color: #c00; font-weight: bold; }
-->
.hiddenRow  { display: none; }
.testcase   { margin-left: 2em; }


/* -- ending ---------------------------------------------------------------------- */
#ending {
}

</style>
"""

    # -----------------------标题-------------------------------------------------

    HEADING_TMPL = """<div class='heading'>
<h1 style="color:#fafafa;letter-spacing: 0;
text-shadow: 0px 1px 0px #999, 0px 2px 0px #888, 0px 3px 0px #777, 0px 4px 0px #666,
 0px 5px 0px #555, 0px 6px 0px #444, 0px 7px 0px #333, 0px 8px 7px #001135">%(title)s</h1>
 <style>
#parameters{
margin-top: 1ex;
margin-bottom: 0;
font-family:"华文行楷";
}
</style>
<p id='parameters'>%(parameters)s</p>
<style>
.description{
margin-top: 4ex;
margin-bottom: 6ex;
font-family:"华文行楷";
}
</style>
<p class='description'>%(description)s</p>
</div>

"""
# 变量: (title, parameters, description)

    HEADING_ATTRIBUTE_TMPL = """<p class='attribute'><strong>%(name)s:</strong> %(value)s</p>
"""
# 变量: (name, value)

    # -------------------------报告-----------------------------------------------

    REPORT_TMPL = """
<style>
#show_detail_line_summary{
background-color:#CC00CC;
width: 46px;
height: 24px;
color: #FFFFFF;
font-family:"华文行楷";
}
#show_detail_line_fail{
background-color:#FF3333;
width: 46px;
height: 24px;
color: #FFFFFF;
font-family:"华文行楷";
}
#show_detail_line_all{
background-color:#6600FF;
width: 46px;
height: 24px;
color: #FFFFFF;
font-family:"华文行楷";
}
</style>
<p>
<button id='show_detail_line_summary' type="button" onclick="javascript:showCase(0)"
 onmouseover="this.style.backgroundColor='#FF6699';" onmouseout="this.style.backgroundColor='#CC00CC';">概要</button>
<button id='show_detail_line_fail' type="button" onclick="javascript:showCase(1)"
onmouseover="this.style.backgroundColor='#FF9933';" onmouseout="this.style.backgroundColor='#FF3333';">失败</button>
<button id='show_detail_line_all' type="button" onclick="javascript:showCase(2)"
 onmouseover="this.style.backgroundColor='#33FF66';" onmouseout="this.style.backgroundColor='#6600FF';">所有</button>
</p>


<table id='result_table'>
<colgroup>
<col align='left' />
<col align='right' />
<col align='right' />
<col align='right' />
<col align='right' />
<col align='right' />
</colgroup>

<style>
#header_row {
    font-weight: bold;
    color: white;
    background-color: #777;
    font-family:"华文行楷";
}
</style>

<style>
.passClass  { background-color: #66FF33;}
.failClass  { background-color: #FF6633;}
.errorClass { background-color: #FF0000;}
.passCase   { color: #66FF33;}
.failCase   { color: #FF6633; font-weight: bold;}
.errorCase  { color: #FF0000; font-weight: bold;}
</style>

<tr id='header_row'>
    <td>测试套件/测试用例</td>
    <td>总数</td>
    <td>通过</td>
    <td>失败</td>
    <td>错误</td>
    <td>查看</td>
</tr>
%(test_list)s

<style>
#total_row  { font-weight: bold;font-family:"华文行楷"; }
</style>
<tr id='total_row'>
    <td >总计</td>
    <td>%(count)s</td>
    <td>%(Pass)s</td>
    <td>%(fail)s</td>
    <td>%(error)s</td>
    <td>&nbsp;</td>
</tr>
</table>
"""
# 变量: (test_list, count, Pass, fail, error)

    REPORT_CLASS_TMPL = r"""
<tr class='%(style)s'>
    <td>%(desc)s</td>
    <td>%(count)s</td>
    <td>%(Pass)s</td>
    <td>%(fail)s</td>
    <td>%(error)s</td>
    <td><a href="javascript:showClassDetail('%(cid)s',%(count)s)">详情</a></td>
</tr>
"""
# 变量: (style, desc, count, Pass, fail, error, cid)

    REPORT_TEST_WITH_OUTPUT_TMPL = r"""
<tr id='%(tid)s' class='%(Class)s'>
    <td class='%(style)s'><div class='testcase'>%(desc)s</div></td>
    <td colspan='5' align='center'>

    <!--css div popup start-->
    <a class="popup_link" onfocus='this.blur();' href="javascript:showTestDetail('div_%(tid)s')" >
        %(status)s</a>

    <div id='div_%(tid)s' class="popup_window">
        <div style='text-align: right; color:red;cursor:pointer'>
        <a onfocus='this.blur();' onclick="document.getElementById('div_%(tid)s').style.display = 'none' " >
           [x]</a>
        </div>
        <pre>
        %(script)s
        </pre>
    </div>
    <!--css div popup end-->

    </td>
</tr>
"""
# 变量: (tid, Class, style, desc, status)

    REPORT_TEST_NO_OUTPUT_TMPL = r"""
<tr id='%(tid)s' class='%(Class)s'>
    <td class='%(style)s'><div class='testcase'>%(desc)s</div></td>
    <td colspan='5' align='center'>%(status)s</td>
</tr>
"""
# 变量: (tid, Class, style, desc, status)

    REPORT_TEST_OUTPUT_TMPL = r"""
%(id)s: %(output)s
"""
# 变量: (id, output)

    # ---------------------------结尾---------------------------------------------

    ENDING_TMPL = """<div id='ending'>&nbsp;</div>"""

# -------------------- 模板类的结束 -------------------


TestResult = unittest.TestResult


class _TestResult(TestResult):

    def __init__(self, verbosity=1):
        super(_TestResult, self).__init__()
        self.stdout0 = None
        self.stderr0 = None
        self.output_buffer = None
        self.success_count = 0
        self.failure_count = 0
        self.error_count = 0
        self.verbosity = verbosity
        self.result = []

    def startTest(self, test):
        super(_TestResult, self).startTest(test)
        self.output_buffer = io.StringIO()
        stdout_redirector.fp = self.output_buffer
        stderr_redirector.fp = self.output_buffer
        self.stdout0 = sys.stdout
        self.stderr0 = sys.stderr
        sys.stdout = stdout_redirector
        sys.stderr = stderr_redirector

    def complete_output(self):
        if self.stdout0:
            sys.stdout = self.stdout0
            sys.stderr = self.stderr0
            self.stdout0 = None
            self.stderr0 = None
        return self.output_buffer.getvalue()

    def stopTest(self, test):
        self.complete_output()

    def addSuccess(self, test):
        self.success_count += 1
        super(_TestResult, self).addSuccess(test)
        output = self.complete_output()
        self.result.append((0, test, output, ''))
        if self.verbosity > 1:
            sys.stderr.write('ok ')
            sys.stderr.write(str(test))
            sys.stderr.write('\n')
        else:
            sys.stderr.write('.')

    def addError(self, test, err):
        self.error_count += 1
        super(_TestResult, self).addError(test, err)
        _, _exc_str = self.errors[-1]
        output = self.complete_output()
        self.result.append((2, test, output, _exc_str))
        if self.verbosity > 1:
            sys.stderr.write('E  ')
            sys.stderr.write(str(test))
            sys.stderr.write('\n')
        else:
            sys.stderr.write('E')

    def addFailure(self, test, err):
        self.failure_count += 1
        super(_TestResult, self).addFailure(test, err)
        _, _exc_str = self.failures[-1]
        output = self.complete_output()
        self.result.append((1, test, output, _exc_str))
        if self.verbosity > 1:
            sys.stderr.write('F  ')
            sys.stderr.write(str(test))
            sys.stderr.write('\n')
        else:
            sys.stderr.write('F')


class HTMLTestRunner(TemplateMixin):
    def __init__(self, stream=sys.stdout, verbosity=1, title=None, description=None):
        self.stream = stream
        self.stop_time = None
        self.verbosity = verbosity
        if title is None:
            self.title = self.DEFAULT_TITLE
        else:
            self.title = title
        if description is None:
            self.description = self.DEFAULT_DESCRIPTION
        else:
            self.description = description

        self.start_time = datetime.datetime.now()

    def run(self, test):
        result = _TestResult(self.verbosity)
        test(result)
        self.stop_time = datetime.datetime.now()
        self.generate_report(result)
        return result

    @staticmethod
    def sort_result(result_list):
        rmap = {}
        classes = []
        for n, t, o, e in result_list:
            cls = t.__class__
            if not(cls in rmap):
                rmap[cls] = []
                classes.append(cls)
            rmap[cls].append((n, t, o, e))
        r = [(cls, rmap[cls]) for cls in classes]
        return r

    def get_report_attributes(self, result):
        start_time = str(self.start_time)[:19]
        self.stop_time = datetime.datetime.now()
        duration = str(self.stop_time - self.start_time)
        status = []
        if result.success_count:
            status.append('通过 %s' % result.success_count)
        if result.failure_count:
            status.append('失败 %s' % result.failure_count)
        if result.error_count:
            status.append('错误 %s' % result.error_count)
        if status:
            status = ' '.join(status)
        else:
            status = 'none'
        return [
            ('开始测试时间', start_time),
            ('运行时长', duration),
            ('状态', status),
        ]

    def generate_report(self, result):
        report_attrs = self.get_report_attributes(result)
        generator = 'HTMLTestRunner %s' % "0.8.2"
        stylesheet = self._generate_stylesheet()
        heading = self._generate_heading(report_attrs)
        report = self._generate_report(result)
        ending = self._generate_ending()
        output = self.html_template % dict(
            title=saxutils.escape(self.title),
            generator=generator,
            stylesheet=stylesheet,
            heading=heading,
            report=report,
            ending=ending,
        )
        self.stream.write(output.encode('utf8'))

    def _generate_stylesheet(self):
        return self.STYLESHEET_TMPL

    def _generate_heading(self, report_attrs):
        a_lines = []
        for name, value in report_attrs:
            line = self.HEADING_ATTRIBUTE_TMPL % dict(
                    name=saxutils.escape(name),
                    value=saxutils.escape(value),
                )
            a_lines.append(line)
        heading = self.HEADING_TMPL % dict(
            title=saxutils.escape(self.title),
            parameters=''.join(a_lines),
            description=saxutils.escape(self.description),
        )
        return heading

    def _generate_report(self, result):
        rows = []
        sorted_result = self.sort_result(result.result)
        for cid, (cls, cls_results) in enumerate(sorted_result):
            np = nf = ne = 0
            for n, t, o, e in cls_results:
                if n == 0:
                    np += 1
                elif n == 1:
                    nf += 1
                else:
                    ne += 1

            if cls.__module__ == "__main__":
                name = cls.__name__
            else:
                name = "%s.%s" % (cls.__module__, cls.__name__)
            doc = cls.__doc__ and cls.__doc__.split("\n")[0] or ""
            desc = doc and '%s: %s' % (name, doc) or name

            row = self.REPORT_CLASS_TMPL % dict(
                style=ne > 0 and 'errorClass' or nf > 0 and 'failClass' or 'passClass',
                desc=desc,
                count=np+nf+ne,
                Pass=np,
                fail=nf,
                error=ne,
                cid='c%s' % (cid+1),
            )
            rows.append(row)

            for tid, (n, t, o, e) in enumerate(cls_results):
                self._generate_report_test(rows, cid, tid, n, t, o, e)

        report = self.REPORT_TMPL % dict(
            test_list=''.join(rows),
            count=str(result.success_count+result.failure_count+result.error_count),
            Pass=str(result.success_count),
            fail=str(result.failure_count),
            error=str(result.error_count),
        )
        return report

    def _generate_report_test(self, rows, cid, tid, n, t, o, e):
        # e.g. 'pt1.1', 'ft1.1', etc
        has_output = bool(o or e)
        tid = (n == 0 and 'p' or 'f') + 't%s.%s' % (cid+1, tid+1)
        name = t.id().split('.')[-1]
        doc = t.shortDescription() or ""
        desc = doc and ('%s: %s' % (name, doc)) or name
        tmpl = has_output and self.REPORT_TEST_WITH_OUTPUT_TMPL or self.REPORT_TEST_NO_OUTPUT_TMPL

        if isinstance(o, str):
            uo = o
        else:
            uo = o
        if isinstance(e, str):
            ue = e
        else:
            ue = e

        script = self.REPORT_TEST_OUTPUT_TMPL % dict(
            id=tid,
            output=saxutils.escape(uo+ue),
        )

        row = tmpl % dict(
            tid=tid,
            Class=(n == 0 and 'hiddenRow' or 'none'),
            style=n == 2 and 'errorCase' or (n == 1 and 'failCase' or 'none'),
            desc=desc,
            script=script,
            status=self.STATUS[n],
        )
        rows.append(row)
        if not has_output:
            return

    def _generate_ending(self):
        return self.ENDING_TMPL


class TestProgram(unittest.TestProgram):

    def runTests(self):
        if self.testRunner is None:
            self.testRunner = HTMLTestRunner(verbosity=self.verbosity)
        unittest.TestProgram.runTests(self)

main = TestProgram


if __name__ == "__main__":
    main(module=None)
