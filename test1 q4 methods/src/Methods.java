
public class Methods {
	
	public Methods() {}
	
	public double averageListNum(double[] numlist){
		int listSum = 0;
		
		for (int i = 0; i < numlist.length; i++) {
			listSum += numlist[i];
		}
		
		float avg = listSum / numlist.length;
		System.out.println(avg);
		return avg;
	}
	
	public void reverseList(String[] varlist) {
		for (int i = varlist.length-1; i >= 0; i--){
			System.out.println(varlist[i]);
		}
	}

}
