package com.lero.util;

import java.sql.Connection;
import java.sql.DriverManager;

public class DbUtil {
	
	public Connection getCon(){
		Connection con=null;
		/*Class.forName(PropertiesUtil.getValue("jdbcName"));
		Connection con = DriverManager.getConnection(PropertiesUtil.getValue("dbUrl"), PropertiesUtil.getValue("dbUserName"), PropertiesUtil.getValue("dbPassword"));
		*/
		try {
			Class.forName("com.mysql.jdbc.Driver");
			con = DriverManager.getConnection("jdbc:mysql://localhost:3306/db_dorm", "root", "");
		} catch (Exception e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		
		return con;
	}
	
	public void closeCon(Connection con) throws Exception {
		if(con!=null) {
			con.close();
		}
	}
	
	public static void main(String[] args) {
		DbUtil dbUtil = new DbUtil();
		try {
			dbUtil.getCon();
		} catch (Exception e) {
			// TODO Auto-generated catch block
			System.out.println("no");
			e.printStackTrace();
		}
	}
}
