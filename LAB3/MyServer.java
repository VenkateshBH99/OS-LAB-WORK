import java.rmi.*;
import java.rmi.registry.*;
public class MyServer{
	public static void main(String agrs[]){
		try{
			Adder stub=new AdderRemote();
			Naming.rebind("rmi://localhost:5000/venkateshbh",stub);
			//System.out.println(stub.add(34,4));

		}catch(Exception e){
			e.printStackTrace();
		}
	}
}