#include "common.h"

void ode_func(const state_type &x, state_type &dxdt, double t) {
    for (int i = 0; i < state_type::size(); i++) {
        dxdt[i] = 0.0;
    }
    // set dx/dt equal to v
    for (int i = 0; i < n * dim; i++) {
        dxdt[i] = x[n * dim + i];
    }

    // calculate dissipation
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < dim; j++) {
            int k = n * dim + i * dim + j;
            dxdt[k] += -k_diss * x[k] / m[i];
        }
    }

    // calculate potential
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (i == j) {continue;}
            double r2 = 0;
            for (int k = 0; k < dim; k++) {
                r2 += pow(x[i * dim + k] - x[j * dim + k], 2);
            }
            double temp_force = -G * m[j] / pow(r2, 1.5);
            for (int k = 0; k < dim; k++) {
                dxdt[n * dim + i * dim + k] += temp_force * x[i * dim + k];
            }
        }
    }
}
