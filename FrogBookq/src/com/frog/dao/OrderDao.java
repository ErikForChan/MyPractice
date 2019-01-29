package com.frog.dao;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.ArrayList;
import java.util.List;
import java.util.Set;

import com.frog.bean.Book;
import com.frog.bean.Cart;
import com.frog.bean.Order;
import com.frog.bean.OrderItem;
import com.frog.bean.User;

public class OrderDao {

	public OrderDao() {
		// TODO Auto-generated constructor stub
	}
	
	public void addOrder(Order order) {
		// TODO Auto-generated method stub
		Connection con=JdbcUtil.getConnection();
		PreparedStatement ps=null;
		String sql="insert into orders(bookname,ordertime,price,count,totalprice,username,address,phone) value(?,?,?,?,?,?,?,?);";
		try{
			ps=con.prepareStatement(sql);
			ps.setString(1, order.getBookname());
			ps.setString(2, order.getOrdertime());
			ps.setInt(3, order.getPrice());
			ps.setInt(4, order.getCount());
			ps.setInt(5, order.getTotalprice());
			ps.setString(6, order.getUsername());
			ps.setString(7, order.getAddress());
			ps.setString(8, order.getPhone());
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
	
	public List<Order> findByName(String userName){
		Connection con=JdbcUtil.getConnection();
		PreparedStatement ps=null;
		ResultSet rs=null;
		String sql="select * from orders where username= ?;";
		System.out.println("执行前");
		List<Order> list = new ArrayList<Order>();
		
		try{
			
			ps=con.prepareStatement(sql);
			ps.setString(1, userName);
			rs=ps.executeQuery();
			while(rs.next()){	
				System.out.println("执行中");
				Order order=new Order();
				order.setBookname(rs.getString(1));
				order.setOrdertime(rs.getString(2));
				order.setPrice(rs.getInt(3));
				order.setCount(rs.getInt(4));
				order.setTotalprice(rs.getInt(5));
				order.setUsername(rs.getString(6));
				order.setAddress(rs.getString(7));
				order.setPhone(rs.getString(8));
				list.add(order);
			}
		//	System.out.println(user.getUsername());
			System.out.println("执行后");
			return list;
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

	public void cutOrder() {
		// TODO Auto-generated method stub
		Connection con=JdbcUtil.getConnection();
		PreparedStatement ps=null;
		ResultSet rs=null;
		String sql="delete from orders";
		System.out.println("执行前");
		try{
			ps=con.prepareStatement(sql);
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
