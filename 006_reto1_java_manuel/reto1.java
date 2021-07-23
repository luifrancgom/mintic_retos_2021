import java.util.Scanner;
public class reto1 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = Integer.parseInt(sc.nextLine());
        
        String datos[] = sc.nextLine().split(" ");
        double datos_num[] = new double[n];
        double suma = 0;
        double prom = 0;
        double medio = 0;
        double bajo = 0;
        for(int i = 0; i<n;i++){
            datos_num[i] = Double.parseDouble(datos[i]);
            suma = suma + datos_num[i]; 
            prom = suma / n;
        
            if (datos_num[i] >= 14.1 && datos_num[i] <= 35) {
                medio += 1;
                
            }
            else if (datos_num[i] >= 5.1 && datos_num[i] <= 14) {
                bajo += 1;
                
            }
            
        }
        int invi_sani = 0;
        if (prom >= 80.1 && prom <= 100) {
            System.out.println("INVIABLE SANITARIAMENTE");
            invi_sani +=1;
            
        }
        else if (prom >= 35.1 && prom <= 80) {
            System.out.println("ALTO");
        }
        else if (prom >= 14.1 && prom <= 35) {
            System.out.println("MEDIO");
        }
        else if (prom >= 5.1 && prom <= 14) {
            System.out.println("BAJO");
        }
        else if (prom >= 0 && prom <= 5) {
            System.out.println("SIN RIESGO");
        }
        System.out.println(String.format("%.2f",((medio + bajo)/n)*100));

        if (invi_sani >= 1) {
            System.out.println("SI");
            }
        else if (invi_sani <= 0) {
            System.out.println("NO");
            }

        sc.close();
        
   }
}