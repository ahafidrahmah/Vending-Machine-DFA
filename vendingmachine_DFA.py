class DFA:
    def __init__(self, config_file):
        self.states = set()
        self.alphabet = set()
        self.start_state = None # status awal
        self.accept_states = set() 
        self.reject_states = set()
        self.transitions = {} # transisi antar status
        self.drink_prices = {"A": 3000, "B": 4000, "C": 6000}
        self.load_config(config_file) # load konfigurasi mesin
        self.balance = 0  # saldo uang yang diterima mesin
        self.current_state = self.start_state # status mesin saat ini
        if self.start_state not in self.states:
            raise ValueError("Start State Tidak Terdefinisi") #memastikan start state valid

        self.trace = [self.current_state] # jejak status mesin

    def load_config(self, file_name): # load konfigurasi mesin
        with open(file_name, 'r') as file:
            section = None
            for line in file:
                line = line.strip()
                if not line or line.startswith('#'): # abaikan baris kosong atau komentar
                    continue
                
                # baca konfigurasi mesin
                if line.startswith('States:'):
                    self.states = set(line.split(':')[1].strip().split(', '))
                elif line.startswith('Alphabet:'):
                    self.alphabet = set(line.split(':')[1].strip().split(', '))
                elif line.startswith('Start:'):
                    self.start_state = line.split(':')[1].strip()
                elif line.startswith('Accept:'):
                    self.accept_states = set(line.split(':')[1].strip().split(', '))
                elif line.startswith('Reject:'):
                    self.reject_states = set(line.split(':')[1].strip().split(', '))
                elif line.startswith('Transitions:'):
                    section = 'transitions'
                elif section == 'transitions':
                    parts = line.split()
                    if len(parts) == 3:
                        state_from, symbol, state_to = parts
                        if state_from not in self.transitions:
                            self.transitions[state_from] = {}
                        self.transitions[state_from][symbol] = state_to
    
    def masukan_uang(self, amount):
        if amount not in {1000, 2000, 5000, 10000}:
            print("Harap masukkan nominal yang dapat diterima! (Pecahan 1000, 2000, 5000 atau 10000)")
            print(f"Current state: {self.current_state}")
            return
        if self.balance + amount > 10000:
            print("Jumlah yang diterima melebihi batas maksimal Rp10000!")
            print(f"Current state: {self.current_state}")
            return
        
        # update saldo dan status mesin
        self.balance += amount
        # transisi ke status berikutnya
        next_state = self.transitions.get(self.current_state, {}).get(str(amount), None)
        
        if next_state and next_state in self.states:
            self.current_state = next_state
            self.trace.append(self.current_state)
        else:
            print("Transisi tidak valid, tetap di state saat ini.")
        
        available_drinks = self.minuman_available()
        if available_drinks:
            print(f"ON: {', '.join(available_drinks)}")
        print(f"Saldo saat ini: Rp{self.balance}")
        print(f"Lintasan DFA: {' → '.join(self.trace)}")
            
    def minuman_available(self):
        available = []
        if self.balance >= 3000: available.append("Minuman A")
        if self.balance >= 4000: available.append("Minuman B")
        if self.balance >= 6000: available.append("Minuman C")
        return available

    def beli_minum(self, choice):
        if choice in self.drink_prices:
            if self.balance >= self.drink_prices[choice]:
                change = self.balance - self.drink_prices[choice]
                print(f"Lintasan DFA: {' → '.join(self.trace)}")
                print(f"Minuman {choice} dapat dibeli. Status: ACCEPTED.")
                if change > 0:
                    print(f"Kembalian: {change}")
                print("Terima kasih! Silakan ambil minuman Anda.")
                exit()
            else:
                print("Saldo tidak cukup. Status: REJECTED")       
        else:
            print("Pilihan minuman tidak valid. Status: REJECTED")
        print(f"Lintasan DFA: {' → '.join(self.trace)}")
            
        

def main():
    dfa = DFA("DFA.txt")
    
    while True:
        try:
            user_input = input("Masukkan uang atau beli minuman (1000, 2000, 5000, 10000, A, B, C): ").strip()
            if not user_input:
                break
            
            if user_input.isdigit():  # masukan norminal uang
                dfa.masukan_uang(int(user_input))
            else:  # pemilihan minuman
                dfa.beli_minum(user_input)
        except KeyboardInterrupt:
            break

if __name__ == "__main__":
    main()
