#include <iostream>
#include <vector>
#include <random>
#include <cmath>
#include <fstream>
#include <sstream> // 👈 NUEVO

using namespace std;

// Estados
const int S = 0;
const int I = 1;
const int R = 2;
const int D = 3;

// Parámetros
const int N = 1000;
const int DAYS = 365;

double beta_rate = 0.3;
double gamma_rate = 0.1;
double mu_rate = 0.01;

// Vecinos
int dx[4] = {-1, 1, 0, 0};
int dy[4] = {0, 0, -1, 1};


// ✅ FUNCIÓN NUEVA
void guardarFrame(const vector<vector<int>>& grid, int dia) {
    stringstream nombre;
    nombre << "data/frame_seq_" << dia << ".csv"; // ✅ FIX

    ofstream file(nombre.str());

    for (const auto& fila : grid) {
        for (size_t j = 0; j < fila.size(); j++) {
            file << fila[j];
            if (j < fila.size() - 1) file << ",";
        }
        file << "\n";
    }

    file.close();
}


int main() {
    vector<vector<int>> grid(N, vector<int>(N, S));
    vector<vector<int>> new_grid = grid;

    random_device rd;
    mt19937 gen(rd());
    uniform_real_distribution<> dis(0.0, 1.0);

    // Infectar una persona inicial
    grid[N/2][N/2] = I;

    ofstream file("output_seq.csv");
    file << "day,S,I,R,D\n";

    for (int day = 0; day < DAYS; day++) {

        int countS = 0, countI = 0, countR = 0, countD = 0;

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {

                int state = grid[i][j];

                if (state == S) {
                    int infected_neighbors = 0;

                    for (int k = 0; k < 4; k++) {
                        int ni = i + dx[k];
                        int nj = j + dy[k];

                        if (ni >= 0 && ni < N && nj >= 0 && nj < N) {
                            if (grid[ni][nj] == I) {
                                infected_neighbors++;
                            }
                        }
                    }

                    if (infected_neighbors > 0) {
                        double prob = 1 - pow((1 - beta_rate), infected_neighbors);
                        if (dis(gen) < prob) {
                            new_grid[i][j] = I;
                        } else {
                            new_grid[i][j] = S;
                        }
                    } else {
                        new_grid[i][j] = S;
                    }
                }
                else if (state == I) {
                    double r = dis(gen);

                    if (r < mu_rate) {
                        new_grid[i][j] = D;
                    }
                    else if (r < mu_rate + gamma_rate) {
                        new_grid[i][j] = R;
                    }
                    else {
                        new_grid[i][j] = I;
                    }
                }
                else {
                    new_grid[i][j] = state;
                }

                // Conteo
                if (new_grid[i][j] == S) countS++;
                else if (new_grid[i][j] == I) countI++;
                else if (new_grid[i][j] == R) countR++;
                else if (new_grid[i][j] == D) countD++;
            }
        }

        grid = new_grid;

        // ✅ GUARDAR FRAME AQUÍ
        guardarFrame(grid, day);

        file << day << "," << countS << "," << countI << "," << countR << "," << countD << "\n";

        cout << "Day " << day << " I=" << countI << endl;
    }

    file.close();

    cout << "Simulación terminada. Resultados en output_seq.csv" << endl;

    return 0;
}