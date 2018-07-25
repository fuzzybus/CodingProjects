// Risk calculator by Fuzzybus 10th July 2018. Updated 25th July 2018

riskCalc();
vars
	player_1: Decimal [4,2]; player_2: Decimal [4,2];
	spread: Decimal [4,2]; bet: Decimal [7,2]; winnings: Decimal [7,2];
	action_1: String; action_2: String;
begin
	read player_1; read player_2; read bet;
	winnings := bet * player_1;
	spread := player_1 - player_2;
		
		if player_2 > player_1
			then spread := - (spread);
		endif;
		write "Risk factor is equal to: " & spread.display;
		
		if (spread >= 1.40) and (player_1 <= 1.40)
			then action_1 := "Let it ride! Potential winnings are: $" & winnings.display;
		write action_1;
		endif;
		
		if (spread <= 1.39) or (player_1 >= 1.41) 
			then action_2 := "Hold your horses, no bet! Potential loss is: $" & bet.display;
			write action_2;
		endif;
end;
