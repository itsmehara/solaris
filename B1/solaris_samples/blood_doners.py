vizag_donors_list = """
Nitesh akula	UnAvailable	9533395308		Report
Rajasekhar Juvvina	Available	9985334815	9492066667	Report
mahesh bangari	Available	8142648857		Report
swamy gelli v s ch	Available	9908447887		Report
visweswara rao	Available	9701608399	08963200190	Report
SURESHKPV	UnAvailable	9866440901		Report
P S S karuna Sowjanya	UnAvailable	9866109841		Report
HIMANSHU SHARMA	Available	8008087368		Report
k.LAKSHMAN	Available	9248749252	9912123145	Report
murali krishna	Available	8688733933		Report
rajesh kumar vutti	UnAvailable	9030603032		Report
singa Reddy Kallam	UnAvailable	8978087568	08912528533	Report
Shaik moula	UnAvailable	9949619992		Report
Raja Neelam	UnAvailable	8790333389		Report
Suman Chimata	UnAvailable	9000199183		Report
chikkala venkatesh	UnAvailable	8143399572		Report
PAVAN KUMAR	Available	7416550172		Report
Avinash Garlapati	Available	8886862814		Report
s n n v m sai	UnAvailable	8332048252		Report
Sampath Swaroop Atkuri	Available	9160250883		Report
Karthik Kumar karuturi	Available	9985196999		Report
pothureddy sandeep	UnAvailable	9533912344		Report
Sankara rao rada	Available	9391682514		Report
Aditya Bonka	UnAvailable	9553050780		Report
Ratnakumar	UnAvailable	9985200070		Report
hemalatha	Available	9515437045	nill	Report
N A S SIVA PARASAD	UnAvailable	9394655222	8464930852	Report
venkateswararao	UnAvailable	9652134566		Report
CH.sathish	Available	9908886215		Report
SEKHAR NEMANI	UnAvailable	9030909392		Report
saiphani	UnAvailable	8297996246		Report
santosh chunduri	Available	9642974790		Report
RAYALA SHYAM SUNDAR	UnAvailable	9949242321		Report
naresh devisetty	Available	9052938663		Report
RAVIRAJ	Available	9059189194		Report
Sireesh	Available	9565420251		Report
Pemmu jeevan kumar-pendurti	Available	7396927612		Report
S Srikanth Varma-pendurti	Available	9912108108		Report
Noor mohammad-pendurti	Available	8500658176		Report
"""

vzm_list_2 ="""Nagu	Available	9533450189		Report
Ravi Babu Chelikani	Available	9440252628		Report
Yasarapu Sanyasirao	Available	9154948560		Report
v.naveen kumar (babu)	Available	8142223323	8142223323	Report
YERNAGULA DHANA LAKSHMI	Available	7382690060		Report
sai kumar	Available	8801846800		Report
Balu Mahendra	Available	9010547716		Report"""


KKD_list_3 = """Veerababu ryali	Available	8886567111	8886263111	Report
Madhav Sai.V	Available	9490010279		Report
prasasd amajala	Available	8341641769		Report
sridhar.reddy	UnAvailable	9963430485	08842319454	Report
Kala srinivasrao	UnAvailable	9848413859		Report
M V Rajesh	Available	8106352229		Report
Ravi Shankar	Available	9160462449	2388449	Report
Anvesh	Available	7396116334		Report
Krishna	Available	8008804239		Report
U naga satish	UnAvailable	7873456677		Report
R.K.R.Shankar	Available	9908914944		Report
Ravi Kiran Naidu	Available	8790062777		Report
SRIKANTH	Available	9059811957		Report
s.l.v.s.prakash	UnAvailable	9966154444		Report
juttuka hemanth kumar	Available	9676799331	8096233334	Report
Gopal Karneedi	Available	9550710848		Report
Dikkala srujana	Available	8179628091		Report
G.Siva Rama Krishna	Available	7702009600		Report
K.Meera	Available	9701424164		Report
mohan sai	Available	9182259381		Report
ravi shankar	Available	9908914944		Report
DVVPRABHAKAR	Available	9885779788		Report
P. Durga Prasad	Available	8500445305		Report"""


def main():
    donors = KKD_list_3
    avail_donors = [line for line in donors.splitlines() if "UnAvailable" not in line and len(line) != 0]
    for don in avail_donors:
        donner = don.split("\t")
        print donner[2],"-->", donner[0]


if __name__ == '__main__':
    main()