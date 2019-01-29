<%@ page language="java" import="java.util.*" pageEncoding="UTF-8"%>
<%
String path = request.getContextPath();
String basePath = request.getScheme()+"://"+request.getServerName()+":"+request.getServerPort()+path+"/";
%>

<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">

	<link rel="stylesheet" type="text/css" href="<%=path %>/css/register.css"/>
	
<html>
  <head>
    <base href="<%=basePath%>">
    <meta charset="UTF-8">
    <title>蛙书-注册</title>
   
  <style type="text/css">
   
  </style>

  </head>
  
  <body>

<script type="text/javascript">

</script>

    <div id="head">
    	<table width="100%" height="80px">
			<tr width="100%" height="80px">
				<td width="25%" height="80px" align="right"><img src="${pageContext.request.contextPath}/images/MainLogo.png"></td>
				<td width="75%" height="80px"><img src="${pageContext.request.contextPath}/images/Welcome_Register.png"></td>
			</tr>
		</table>
    </div>
    <br/>
	<div class="whole">
    	<div class="text">
    		<form action="jsp/registerHandler.jsp" method="post">
    			<input type="hidden" name="operation" value="regist"/>
    			<br/>
	    		<table align="center">
	    			<div id="num">
	    				<tr>
	    				<td><B>用户名</B></td>
	    				<td><input style="width:200px;height:40px;" id="username" placeholder="用户名" required=""  type="text" name="username"/></td>
	    				
	    			    </tr>
	    			    <tr height="15px"></tr>
	    			</div>
	    			<div id="pwd">
	    				<tr>
	    				<td><B>密码</B></td>
	    				<td><input style="width:200px;height:40px;"  type="password" placeholder="密码:6到20位之间" pattern=".{6,20}" pm="密码要在6到20位之间" required=""  name="password"/></td>
	    			
	    				<tr height="15px"></tr>
	    			</tr>
	    			</div>

	    			<div id="sex">
	    				<tr>
	    				<td><B>性别</B></td>
	    				<td><input style="width:200px;height:40px;"  type="text" placeholder="性别" required=""  name="sex"/>
	    				</td>
	    			</tr>
	    			<tr height="15px"></tr>
	    			</div>
	    			<div id="email">
	    				<tr>
	    				<td><B>邮箱</B></td>
	    				<td><input style="width:200px;height:40px;"  type="text"  placeholder="邮箱：*****@qq.com" required="" pattern="^\w+([-+.']\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*$" type="text" name="email"/>
	    				</td>
	    			</tr>
	    			<tr height="15px"></tr>
	    			</div>
	    			<div id="phone">
	    				<tr>
	    				<td><B>手机号</B></td>
	    				<td><input style="width:200px;height:40px;" placeholder="手机号" required=""
                        pattern="^1[0-9]{10}$" type="text" name="phone"/></td>
	    			</tr>
	    			<tr height="15px"></tr>
	    			</div>
	    			<div id="address">
	    				<tr>
	    				<td><B>地址</B></td>
	    				<td><input style="width:200px;height:40px;" placeholder="地址" required="" type="text" name="address"/></td>
	    			</tr>
	    			<tr height="15px"></tr>
	    			</div>
	    			<tr>
	    			    <td></td>
	    				<td><a><input class="btn" width="220px"  type="submit" value="提交注册"/></a></td>
	    			</tr>
	    	    </table>
	    	</form>
    	</div>
    	  <div id="foot">
         <p>关于我们| 联系我们|手机蛙书| 友情链接| 销售联盟| 蛙书社区| 蛙书公益| English Site</p>
       	<p>长沙学院2013级软件1班 汇泽2栋337</p>
    	
    </div>
    </div>
  </body>
</html>
