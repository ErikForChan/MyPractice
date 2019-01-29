<%@ page language="java" import="java.util.*" pageEncoding="UTF-8"%>
<%
String path = request.getContextPath();
String basePath = request.getScheme()+"://"+request.getServerName()+":"+request.getServerPort()+path+"/";
%>

<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<link rel="stylesheet" type="text/css" href="<%=path %>/css/login.css"/>
	<title>蛙书-登陆</title>
    <style>
       
    </style>
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
	<p></p>
	<div id="container">
			<div id="form">
				<form action="../loginServlet" method="post">
				      <p id="label1">蛙书登陆</p>		   
                       <div id="input" align="center">
                      <B>用户: </B><input type="text" name="username" placeholder="请输入用户名" required="" > <br/>
                      <B>密码: </B><input type="password" name="password" placeholder="请输入密码" required="" > <br/>
                      </div>
                      <div id="LoginAuto">   
                           <input type="checkbox" align="left">记住密码&nbsp&nbsp&nbsp&nbsp&nbsp
                           <a href="register.jsp">立即注册</a>
                      </div>
                      <div id="button" align="center">
                      	    <input type="submit" value="登  陆">
                       <br/>
                      </div>

                      <div id="belowLogin">
                      	长沙学院汇泽2栋337制作
                      </div> 
				</form>
			</div>
    </div>
    <div id="foot">
        <p>关于我们| 联系我们|手机蛙书| 友情链接| 销售联盟| 蛙书社区| 蛙书公益| English Site</p>
    	<p>长沙学院2013级软件1班 汇泽2栋337</p>
    	
    </div>
</body>
</html>