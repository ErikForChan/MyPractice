package com.frog.dao;
import java.sql.Connection;
import java.sql.DriverManager;

public class JdbcUtil {

	public static Connection getConnection(){
		Connection con=null;
		try{
			Class.forName("com.mysql.jdbc.Driver");
			con=DriverManager.getConnection("jdbc:mysql://localhost:3306/bookshop?useUnicode=true&characterEncoding=UTF-8", "root", "");
		}catch(Exception e){
			e.printStackTrace();
		}
		return con;
	}
	
}
