<%@ page language="java" import="java.util.*" pageEncoding="UTF-8"%>
<%
String path = request.getContextPath();
String basePath = request.getScheme()+"://"+request.getServerName()+":"+request.getServerPort()+path+"/";
%>

<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html>
  <head>
    <base href="<%=basePath%>">
    <link rel="stylesheet" type="text/css" href="<%=path %>/css/left.css"/>
    <title>My JSP 'lest.jsp' starting page</title>
    
	<meta http-equiv="pragma" content="no-cache">
	<meta http-equiv="cache-control" content="no-cache">
	<meta http-equiv="expires" content="0">    
	<meta http-equiv="keywords" content="keyword1,keyword2,keyword3">
	<meta http-equiv="description" content="This is my page">
	<!--
	<link rel="stylesheet" type="text/css" href="styles.css">
	-->
   <script>
           function hiddenDiv(div){
                  div.style.display=(div.style.display=='none'?'block':'none');
           }
    </script>
  </head>
  
  <body>
    <div id="style1">
          <div id="style11">
            <div id="style111">                  
                <div><a href="javascript:void(0)" onclick="hiddenDiv(document.getElementById('style312'))"></a></div>
            </div>
            <div id="style112">
              <ul>
                <li><a href="TypeServlet" target="right" name="software">计算机类</a></li>
                <li><a href="literatureServlet" target="right">文学类</a></li>
                <li><a href="homeServlet" target="right">家庭类</a></li>
              </ul>
            </div>
          </div>
        </div>

        <div id="style2">
          <div id="style21">
            <div id="style211">                  
                <div><a href="javascript:void(0)" onclick="hiddenDiv(document.getElementById('style212'))"></a></div>
            </div>
            <div id="style212">
              <ul>
                <li><a href="lowServlet" target="right">15元以下</a></li>
                <li><a href="betweenServlet" target="right">15--50元</a></li>
                <li><a href="highServlet" target="right">50元以上</a></li>
              </ul>
            </div>
          </div>
        </div>
        
        <div id="style3">
          <div id="style31">
            <div id="style311">                  
                <div><a href="javascript:void(0)" onclick="hiddenDiv(document.getElementById('style312'))"></a></div>
            </div>
            <div id="style312">
              <ul>
                <li><a href="Before2014Servlet" target="right">2014年前</a></li>
                <li><a href="In2014Servlet" target="right">2014年</a></li>
                <li><a href="In2015Servlet" target="right">2015年</a></li>
                <li><a href="In2016Servlet" target="right">2016年</a></li>
                <li><a href="After2016Servlet" target="right">2016年后</a></li>
              </ul>
            </div>
          </div>
        </div>
  </body>
</html>
