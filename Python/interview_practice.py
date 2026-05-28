
class interview_practice:

    def prime_number(self,n):
        for i in range(2, int(n ** 0.5)+1):
            if(n % i == 0):
                return False
        return True

    def palindrome(self, str):
        for i in range(len(str) //2):
            if str[i] == str[-(i + 1)]:
                return True
            return False

    def vowel_replace_space(self, str):
        vow = ['a','e' ,'i' ,'o', 'u']
        new = []
        for i in range(len(str)):
            if str[i].lower() in vow:
                new.append('x')
            else:
                new.append(str[i])

        print("".join(new))

if __name__ == "__main__":
    practice = interview_practice()
    number = 11
    print(f"The number {number} is {'a prime' if practice.prime_number(number) else 'not a prime'} number")

    string = "madam"
    print(f"The string {string} is {'a palindrome' if practice.palindrome(string) else 'not a palindrome'}")

    practice.vowel_replace_space("muni")
    import json
    json_path = "C:\/Study\/Data_Engineer\/Python\/test.json"
    with open(json_path, "r") as file:
        data = json.load(file)
        print(data)