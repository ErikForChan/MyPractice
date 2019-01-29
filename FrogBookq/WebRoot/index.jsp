<%@ page language="java" import="java.util.*" pageEncoding="ISO-8859-1"%>
<%
String path = request.getContextPath();
String basePath = request.getScheme()+"://"+request.getServerName()+":"+request.getServerPort()+path+"/";
%>

<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html>
  <head>
   
  </head>

   <frameset rows="25%,*"  frameborder="1" border="2" framespacing= "5">

              <frame src="userInfoServlet" name="head">

                  <frameset cols="20%,80%"  frameborder="1" border="2" framespacing= "5">
                  <frame src="jsp/left.jsp" name="left">
                  <frame src="jsp/right.jsp" name="right">
                  </frameset>

   </frameset>
</html>
