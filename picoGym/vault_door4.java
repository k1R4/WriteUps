public class vault_door4{

public static void main(String args[]){
    try{
    byte[] myBytes = {
            106 , 85  , 53  , 116 , 95  , 52  , 95  , 98  ,
            0x55, 0x6e, 0x43, 0x68, 0x5f, 0x30, 0x66, 0x5f,
            0142, 0131, 0164, 063 , 0163, 0137, 070 , 0146,
            '4' , 'a' , '6' , 'c' , 'b' , 'f' , '3' , 'b' ,
    };

    String s = new String(myBytes);
    System.out.println(s);
    System.out.flush();
    
    }
    catch(Exception e){
        e.printStackTrace();
    }

}}
