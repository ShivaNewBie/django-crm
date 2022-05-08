import { createStore } from 'vuex'

export default createStore({
  state: { //this are global variables to use 
    isLoading: false,
    isAuthenticated: false,
    token: '',
    user: {
      id:0,
      username:'',
        },
    team: { 
      id: 0,
      name:'',
      plan:'',
      max_leads:0,
      max_clients:0,
    }
  },
  getters: {
  },
  mutations: {
    initializeStore(state){ //this function only inializes an if statement not change any data rather it checks whether the data is authenticated 
      if (localStorage.getItem('token')){ //token determines if the user is authenticated
        state.token = localStorage.getItem('token')
        state.isAuthenticated = true
        state.user.username = localStorage.getItem('username')
        state.user.id = localStorage.getItem('userid')
        state.team.name = localStorage.getItem('team_name')
        state.team.id = localStorage.getItem('team_id')
        state.team.plan = localStorage.getItem('team_plan')
        state.team.max_leads = localStorage.getItem('team_max_leads')
        state.team.max_clients = localStorage.getItem('team_max_clients')
      } else {
        state.token = '' //this is not really necessary so dont think much about it
        state.isAuthenticated = false 
        state.user.id = 0
        state.user.username = ''
        state.team.id = 0
        state.team.name = ''
        state.team.plan = ''
        state.team.max_leads = 0
        state.team.max_clients = 0


      } 
    },
    setIsLoading(state,status){
      state.isLoading = status 
    },
    setToken(state,token){
      state.token = token 
      state.isAuthenticated = true 
    },
    setUser(state,user){
      state.user = user 
    },
    setTeam(state,team){
      state.team = team
      localStorage.setItem('team_id', team.id)
      localStorage.setItem('team_name', team.name)
      localStorage.setItem('team_plan', team.plan)
      localStorage.setItem('team_max_leads', team.max_leads)
      localStorage.setItem('team_max_clients', team.max_clients)

    },

    removeToken(state){
      state.token = ''
      state.isAuthenticated = false 
    }
  },
  actions: {
  },
  modules: {
  }
})
