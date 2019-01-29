package com.frog.dao;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.ArrayList;
import java.util.List;

import com.frog.bean.Book;
import com.frog.bean.Cart;


public class CartDao {

	public CartDao() {
		// TODO Auto-generated constructor stub
	}
	
	public void addCount(String userName,String bookName){
		Connection con=JdbcUtil.getConnection();
		PreparedStatement ps=null;
		ResultSet rs=null;
		String sql="update cart set count=count+1,totalprice=price*count where username=? and bookname=?;";
		System.out.println("执行前");
		try{
			ps=con.prepareStatement(sql);
			ps.setString(1, userName);
			ps.setString(2, bookName);
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
	
	public void cutCount(String userName,String bookName){
		Connection con=JdbcUtil.getConnection();
		//PreparedStatement pst=null;
		PreparedStatement ps=null;
		ResultSet rs=null;
		//String sqlt="select * from cart where username= ? and bookname= ?;";
		String sql="update cart set count=count-1,totalprice=price*count where username=? and bookname=?;";
		System.out.println("执行前");
		try{
			/*pst=con.prepareStatement(sqlt);
			pst.setString(1, userName);
			pst.setString(2, bookName);
			rs=pst.executeQuery();
			int countt=rs.getInt(5);
			System.out.println(countt);*/
			//if(countt>0){
				ps=con.prepareStatement(sql);
				ps.setString(1, userName);
				ps.setString(2, bookName);
				ps.executeUpdate();
		//	}
			
		}catch(Exception e){
			e.printStackTrace();
		}
		try {
		//	if(pst!=null)pst.close();
			if(ps!=null)ps.close();
			con.close();
		} catch (SQLException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}
	
	public void cutCart(String userName,String bookName){
		Connection con=JdbcUtil.getConnection();
		PreparedStatement ps=null;
		ResultSet rs=null;
		String sql="delete from cart where username=? and bookname=?;";
		System.out.println("执行前");
		try{
			ps=con.prepareStatement(sql);
			ps.setString(1, userName);
			ps.setString(2, bookName);
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
	
	public void cutCart(String userName){
		Connection con=JdbcUtil.getConnection();
		PreparedStatement ps=null;
		ResultSet rs=null;
		String sql="delete from cart where username=?;";
		System.out.println("执行前");
		try{
			ps=con.prepareStatement(sql);
			ps.setString(1, userName);
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
	
	public List<Cart> findByName(String userName){
		Connection con=JdbcUtil.getConnection();
		PreparedStatement ps=null;
		ResultSet rs=null;
		String sql="select * from cart where username= ?;";
		System.out.println("执行前");
		List<Cart> list = new ArrayList<Cart>();
		
		try{
			
			ps=con.prepareStatement(sql);
			ps.setString(1, userName);
			rs=ps.executeQuery();
			while(rs.next()){	
				System.out.println("执行中");
				Cart cart=new Cart();
				cart.setUsername(rs.getString(1));
				cart.setImgURL(rs.getString(2));
				cart.setBookname(rs.getString(3));
				cart.setPrice(rs.getInt(4));
				cart.setCount(rs.getInt(5));
				cart.setTotalprice(rs.getInt(6));
				list.add(cart);
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

	/*public Cart findByNameBook(String userName,String bookName){
		Connection con=JdbcUtil.getConnection();
		PreparedStatement ps=null;
		ResultSet rs=null;
		String sql="select * from cart where username= ? and bookname= ?;";
		System.out.println("执行前");
		Cart cart=new Cart();
		
		try{
			
			ps=con.prepareStatement(sql);
			ps.setString(1, userName);
			ps.setString(2, bookName);
			rs=ps.executeQuery();
			while(rs.next()){	
				System.out.println("执行中");
				
				cart.setUsername(rs.getString(1));
				cart.setImgURL(rs.getString(2));
				cart.setBookname(rs.getString(3));
				cart.setPrice(rs.getInt(4));
				cart.setCount(rs.getInt(5));
				cart.setTotalprice(rs.getInt(6));
				return cart;
			}
		//	System.out.println(user.getUsername());
			System.out.println("执行后");
		
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
	}*/
	
	public void addCart(Cart cart) {
		// TODO Auto-generated method stub
		Connection con=JdbcUtil.getConnection();
		PreparedStatement ps=null;
		String sql="insert into cart(username,imgURL,bookname,price,count,totalprice) value(?,?,?,?,?,?);";
		try{
			ps=con.prepareStatement(sql);
			ps.setString(1, cart.getUsername());
			ps.setString(2, cart.getImgURL());
			ps.setString(3, cart.getBookname());
			ps.setInt(4, cart.getPrice());
			ps.setInt(5, cart.getCount());
			ps.setInt(6, cart.getTotalprice());
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
