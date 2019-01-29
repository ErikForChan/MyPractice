<%@ page language="java" import="java.util.*" pageEncoding="UTF-8"%>
<%
String path = request.getContextPath();
String basePath = request.getScheme()+"://"+request.getServerName()+":"+request.getServerPort()+path+"/";
%>

<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html>
  <head>
    <base href="<%=basePath%>">
    <link rel="stylesheet" type="text/css" href="<%=path %>/css/loginError.css"/>
    <title>My JSP 'loginError.jsp' starting page</title>
    

  </head>
  
  <body>
    <div id="head">
		<table width="100%" height="80px">
			<tr width="100%" height="80px">
				<td width="25%" height="80px" align="right"><img src="${pageContext.request.contextPath}/images/MainLogo.png"></td>
				<td width="75%" height="80px"><img src="${pageContext.request.contextPath}/images/Welcome_Login.png"></td>
			</tr>
		</table>
		
	</div>
	<div id="ErrorPage">
	     <div id="ErrorImage"><img alt="" src="images/loginError.png"></div>
	     <div id="loginagain"><a href="jsp/login.jsp"><input type="button" value="重新登陆" ></input></a></div>
	</div>
  </body>
</html>
