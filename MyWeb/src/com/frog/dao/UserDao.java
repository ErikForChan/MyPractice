package com.frog.dao;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.ArrayList;
import java.util.List;

import com.frog.bean.User;

public class UserDao {

	public User findByUserName(String userName){
		Connection con=JdbcUtil.getConnection();
		PreparedStatement ps=null;
		ResultSet rs=null;
		String sql="select * from user where username= ?;";
		User user=new User();
		try{
		
			ps=con.prepareStatement(sql);
			ps.setString(1, userName);
			rs=ps.executeQuery();
			while(rs.next()){
				user.setUsername(rs.getString(1));
				user.setPassword(rs.getString(2));
				user.setSex(rs.getString(3));
				user.setAddress(rs.getString(4));
				user.setEmail(rs.getString(5));
				user.setPhone(rs.getString(6));
				return user;
			}
		//	System.out.println(user.getUsername());

		}catch(Exception e){
			e.printStackTrace();
		}
		try {
		 	if(rs!=null)rs.close();
		 	ps.close();
		 	con.close();
		} catch (SQLException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		return null;
	}

	public List<User> findUsers() {
		Connection con=JdbcUtil.getConnection();
		PreparedStatement ps=null;
		ResultSet rs=null;
		String sql="select * from user";	
		List<User> list = new ArrayList<User>();
		try{
			ps=con.prepareStatement(sql);
			rs=ps.executeQuery();
			while(rs.next()){
			
				User user = new User();
				user.setUsername(rs.getString(1));
				user.setPassword(rs.getString(2));
				user.setSex(rs.getString(3));
				user.setAddress(rs.getString(4));
				user.setEmail(rs.getString(5));
				user.setPhone(rs.getString(6));
				list.add(user);
			}
			return list;
		}catch(Exception e){
			e.printStackTrace();
		}
		try {
			rs.close();
			ps.close();
			con.close();
		} catch (SQLException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		return null;
	}

	public void addUser(User user) {
		// TODO Auto-generated method stub
		Connection con=JdbcUtil.getConnection();
		PreparedStatement ps=null;
		String sql="insert into user(username,password,sex,address,email,phone) value(?,?,?,?,?,?);";
		try{
			ps=con.prepareStatement(sql);
			ps.setString(1, user.getUsername());
			ps.setString(2, user.getPassword());
			ps.setString(3, user.getSex());
			ps.setString(4, user.getAddress());
			ps.setString(5, user.getEmail());
			ps.setString(6, user.getPhone());
			ps.executeUpdate();
		}catch(Exception e){
			e.printStackTrace();
		}
		try {
			ps.close();
			con.close();
		} catch (SQLException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}
	
}
