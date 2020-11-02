#include <fstream>
#include <boost/array.hpp>
#include <boost/numeric/odeint.hpp>

#include "common.h"

using namespace std;
using namespace boost::numeric::odeint;

fstream out;

void ode_func(const state_type &x, state_type &dxdt, double t);

void write_state(const state_type &x, const double t) {
    out << t << '\t';
    for (auto coord : x) {
        out << coord << '\t';
    }
    out << endl;
}


int main() {
    out.open("path.txt");

    state_type x = {0, 152E9, 0, 0, 30E3, 0, 0, 0};
    double duration = 1 * 365 * 24 * 3600;
    int nsteps = 1E3;

    integrate_const( make_dense_output( 1.0e-6 , 1.0e-6 ,runge_kutta_dopri5< state_type >() ) ,
                     ode_func , x , 0.0 , duration , duration / nsteps, write_state);

    out.close();
    return 0;
}
