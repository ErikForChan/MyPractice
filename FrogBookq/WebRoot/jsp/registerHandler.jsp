<%@page import="java.sql.*"%>
<%@page import="javax.naming.*"%>
<%@page import="javax.activation.DataSource"%>
<%@page import="com.frog.dao.*"%>
<%@page import="com.frog.bean.*"%>
<%@ page language="java" import="com.frog.bean.User" %>
<%@ page language="java" import="java.util.*" pageEncoding="UTF-8"%>
<%
String path = request.getContextPath();
String basePath = request.getScheme()+"://"+request.getServerName()+":"+request.getServerPort()+path+"/";
%>

<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html>
  <head>
    <base href="<%=basePath%>">
    
    <title>My JSP 'registerHandler.jsp' starting page</title>

  </head>
  
  <body>
    <jsp:useBean id="user" class="com.frog.bean.User"></jsp:useBean>
    <jsp:setProperty property="*" name="user"/>

    <%
      boolean flag=false;
      Connection con=null;
      PreparedStatement pst=null;
    
             try{
			  con=JdbcUtil.getConnection();
			  con.setAutoCommit(false);		    
			  String sql="insert into user(username,password,sex,address,email,phone)values(?,?,?,?,?,?);";
              pst=con.prepareStatement(sql);
              pst.setString(1, user.getUsername());
              pst.setString(2, user.getPassword());
              pst.setString(3, user.getSex());
              pst.setString(4, user.getAddress());
              pst.setString(5, user.getEmail());
              pst.setString(6, user.getPhone());
              pst.executeUpdate();
              con.commit();
              flag=true;
              pst.close();
              con.close();
		     }catch(Exception e){
			 e.printStackTrace();
	       	}
	  	   
              
              if(flag){
              request.getRequestDispatcher("/jsp/registerSuccess.jsp").forward(request,response);          
                 
              }else{
                  out.print("注册失败!");
              }
	   
     %>
  </body>
</html>
