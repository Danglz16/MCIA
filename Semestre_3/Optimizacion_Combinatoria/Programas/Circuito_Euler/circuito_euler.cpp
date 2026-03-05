#include <iostream>
#define MAXVNUM	50

using namespace std;

class Mgraph;
class Edge;

class Edge{
friend class Mgraph;
public:
	Edge()	{mark=0;};
private:
	int v[2];
	Edge *next[2];
	int mark;
};

class Mgraph{
public:
	Mgraph();
	void input();
        void eulercycle();
	void eulercycle(int currentv);
	Edge *nextedge(int cv);
private:
	int n;
        int e;
	Edge *vertex[MAXVNUM];
};

Mgraph::Mgraph(){

  int i;

  for(i=0;i<MAXVNUM;i++)
    vertex[i]=0;
}

void Mgraph::input(){

  int i;
  Edge *te;

  cout<<"Please enter the number of vertices and edges:";
  cin>>n>>e;
  cout<<"Please enter the edges"<<endl;

  for(i=0;i<e;i++){
    te=new Edge();
    cin>>te->v[0]>>te->v[1];
    cout<<te->v[0]<< " " <<te->v[1]<<endl;
    te->next[0]=vertex[te->v[0]];
    vertex[te->v[0]]=te;
    te->next[1]=vertex[te->v[1]];
    vertex[te->v[1]]=te;
  }
  cout << "edges: " << e << " vertices: " << n << endl;
}

Edge *Mgraph::nextedge(int cv){

  
  Edge *te,*tmp;

  te=vertex[cv];
  while(te && te->mark){
    tmp=te;
    if(cv==te->v[0])
      te=te->next[0];
    else
      te=te->next[1];
    delete tmp;
  }
  if(te){
    te->mark=1;
    if(cv==te->v[0])
      vertex[cv]=te->next[0];
    else
      vertex[cv]=te->next[1];
    return te;
  }
  vertex[cv]=0;
  return 0;
}

void Mgraph::eulercycle(int currentv){
  #include<iostream>

  Edge *ce;

  while((ce=nextedge(currentv))){
    if(currentv==ce->v[0])
    {
      eulercycle(ce->v[1]);
    }
    else
    {
      eulercycle(ce->v[0]);
    }
    }
  cout<<currentv<<"  ";
  return;
}

void Mgraph::eulercycle(){
  
  cout<<"The Euler cycle of this graph is"<<endl;
  eulercycle(1);
  cout<<endl;
}

int main()
{
  Mgraph mg;

  mg.input();
  mg.eulercycle();
}
