#include <cstdlib> //заголовок для стандартной библиотеки С 
#include <iostream> //заголовок для поддержки системы ввода-вывода в С++ 
#include <iomanip> 
#include <fstream>

using namespace std;
ofstream f;
ofstream c;

struct DATA_FACTORY {
	int number;
	string district;
	string company_name;
	float commercial_products;
	float cost;
	int workers;
	float productivity;
	float foundation;
	float volume_of_commercial_products;
 };


const int n = 20; //Array size
DATA_FACTORY data_array[n];
void data_input();
void get_up_and_down();
void create_tab();
void max_company();
void show_volume_of_commercial_products();
void sorting();
void itog();
void (*menu[7])() = { data_input, get_up_and_down, create_tab, max_company, show_volume_of_commercial_products, itog, sorting };

int main(){
	cout << "\n<<Консоль>>"; 
	cout << "\n1 Ввод данных;"; 
	cout << "\n2 Получить верхнюю и нижнюю границы выпуска товарной продукции;"; 
	cout << "\n3 Создать таблицу на интервале товарной продукцией;";
	cout << "\n4 Пффолучить предприятие с наибольшей фондоотдачей  и с наибольшей производительностью труда;"; 
	cout << "\n5 Получить сведения об объеме выпуска товарной продукции;"; 
	cout << "\n6 Итого;"; 
	cout << "\n7 Чтобы выйти из меню.\n";
	while(1){
		cout << "\n>> ";
		int m;
		cin >> m;
		cout << endl;
		if (m == 7) break;
		menu[m-1]();

	}
	return 0;
}

void data_input(){
	cout << "Введите данные:\n";
	cout << "Чтобы завершить ввод, введите 0\n\n";
	
	for (int i = 0; i < n; i++){
		if (data_array[i].number == NULL){
				if (data_array[i].number == i+1) break;
				cout << "Number: " << i+1 << endl;
				cout << "District >> ";
				cin >> data_array[i].district; 
				if (data_array[i].district == "0") break; 

				data_array[i].number = i+1;

				cout << "Company name >> "; 
				cin >> data_array[i].company_name; 
				if (data_array[i].company_name == "0") break; 
				cout << "Commercial products #ц.цц >> "; 
				cin >> data_array[i].commercial_products; 
				if (data_array[i].commercial_products == 0) break; 
				cout << "Cost #ц.цц >> "; 
				cin >> data_array[i].cost; 
				if (data_array[i].cost == 0) break; 
				cout << "Workers #ц >> "; 
				cin >> data_array[i].workers; 
				if (data_array[i].workers == 0) break;
				data_array[i].volume_of_commercial_products = data_array[i].commercial_products + data_array[i].cost; //Объём выпуска товарной продукции
				cout << "Volume of commercial products: " << data_array[i].volume_of_commercial_products << "\n";
				data_array[i].productivity = data_array[i].volume_of_commercial_products / data_array[i].workers;
				cout << "Productivity: " << data_array[i].productivity << "\n"; 
				data_array[i].foundation = data_array[i].volume_of_commercial_products / data_array[i].cost;
				cout << "Foundation: " << data_array[i].foundation << "\n"; 
				f << data_array[i].number << "\t" << data_array[i].district << "\t" << data_array[i].company_name << "\t" << data_array[i].commercial_products << "\t" << data_array[i].cost << "\t" << data_array[i].workers << "\t" << data_array[i].productivity << "\t" << data_array[i].foundation << "\t" << data_array[i].volume_of_commercial_products << "\n";

 			} 
 		} 
 	menu[6]();
}

void sorting(){
	f.open("out_file.txt", ios::out );
	for (int i = 0; i < n; i++){
		for (int j = i+1; j < n-1; j++){
			if (data_array[i].number == NULL or data_array[j].number == NULL) break;
			if (data_array[i].productivity < data_array[j].productivity){
				swap(data_array[i].number, data_array[j].number);
				swap(data_array[i].district, data_array[j].district);
				swap(data_array[i].company_name, data_array[j].company_name);
				swap(data_array[i].commercial_products, data_array[j].commercial_products);
				swap(data_array[i].cost, data_array[j].cost);
				swap(data_array[i].workers, data_array[j].workers);
				swap(data_array[i].productivity, data_array[j].productivity);
				swap(data_array[i].foundation, data_array[j].foundation);
				swap(data_array[i].volume_of_commercial_products, data_array[j].volume_of_commercial_products);
			}
		}
	}
	for (int i = 0; i < n; i++){
		if (data_array[i].number == NULL) break;
		cout << data_array[i].number << endl;
		cout << data_array[i].district << endl;
		cout << data_array[i].company_name << endl;
		cout << data_array[i].commercial_products << endl;
		cout << data_array[i].cost << endl;
		cout << data_array[i].workers << endl;
		cout << data_array[i].productivity << endl;
		cout << data_array[i].foundation << endl;
		cout << data_array[i].volume_of_commercial_products << endl;
		f << data_array[i].number << "\t" << data_array[i].district << "\t" << data_array[i].company_name << "\t" << data_array[i].commercial_products << "\t" << data_array[i].cost << "\t" << data_array[i].workers << "\t" << data_array[i].productivity << "\t" << data_array[i].foundation << "\t" << data_array[i].volume_of_commercial_products << "\n";
	}
	f.close();
}

void get_up_and_down(){
	float max_volume = 0.0;
	int max_i;
	int min_i;
	float min_volume = 100000000000.0;
	for (int i = 0; i < n; i++){
		if (data_array[i].number == NULL) break;
		if (data_array[i].volume_of_commercial_products < min_volume){
			min_volume = data_array[i].volume_of_commercial_products;
			min_i = i;
		}
		if (data_array[i].volume_of_commercial_products > max_volume){
			max_volume = data_array[i].volume_of_commercial_products;
			max_i = i;
		}
	}
	cout << "\nВерхняя граница выпуска товарной продукции:\n" << data_array[max_i].company_name << " -> " << data_array[max_i].volume_of_commercial_products;
	cout << "\nНижняя граница выпуска товарной продукции:\n" << data_array[min_i].company_name << " -> " << data_array[min_i].volume_of_commercial_products << endl;

}

void create_tab(){
	c.open("out_file_tab.txt", ios::out );
	float interval_ot, interval_do;

	cout << "Введите интервал:\n";
	cout << "От >> "; cin >> interval_ot;
	cout << "До >> "; cin >> interval_do;
	cout << endl;

	for (int i = 0; i < n; i++){
		if (data_array[i].number == NULL) break;
		if ((data_array[i].commercial_products < interval_do) and (data_array[i].commercial_products > interval_ot) ){
			c << data_array[i].number << "\t" << data_array[i].district << "\t" << data_array[i].company_name << "\t" << data_array[i].commercial_products << "\t" << data_array[i].cost << "\t" << data_array[i].workers << "\t" << data_array[i].productivity << "\t" << data_array[i].foundation << "\t" << data_array[i].volume_of_commercial_products << "\n";
		}
		
	}
	c.close();
}

void max_company(){
	int i_p;
	int i_f;
	float max_productivity = 0.0;
	float max_foundation = 0.0;

	for (int i = 0; i < n; i++){
		if (data_array[i].number == NULL) break;
		if (data_array[i].productivity > max_productivity){
			max_productivity = data_array[i].productivity;
			i_p = i;
		}
		if(data_array[i].foundation > max_foundation){
			max_foundation = data_array[i].foundation;
			i_f = i;
		}
	
	}
	cout << "Предприятие c наибольшей производительностью труда:\n" << data_array[i_p].company_name << endl;
	cout << "Предприятие c наибольшей фондоотдачей:\n" << data_array[i_f].company_name << endl;
}

void show_volume_of_commercial_products(){
	cout << "Сведения об объеме выпуска товарной продукции:\n";
	for (int i = 0; i < n; i++){
		if (data_array[i].number == NULL) break;
		cout << data_array[i].company_name << ": " << data_array[i].volume_of_commercial_products << endl;
	}
}

void itog(){
	float volume_productivity = 0.0;
	float volume_foundation = 0.0;
	cout << "Итого:\n";
	int j = 0;
	for (int i = 0; i < n; i++){
		if (data_array[i].number == NULL) break;
		volume_productivity = volume_productivity + data_array[i].productivity;
		volume_foundation = volume_foundation + data_array[i].foundation;
		j++;
	}

	cout << "Productivity: " << volume_productivity / j << " Foundation: " << volume_foundation / j << endl;


}