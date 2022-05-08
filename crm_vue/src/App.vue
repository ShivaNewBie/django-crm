<template>
  <Navbar />
  
  <div class='is-loading-bar has-text-centered' v-bind:class="{'is-loading': $store.state.isLoading}">
  <div class='lds-dual-ring'></div>
  
    </div>
  <router-view></router-view>

</template>



<script>
import axios from 'axios'
import Navbar from './components/layout/Navbar.vue'


export default {
  name: 'App',
  components:{
    Navbar,
  },
  beforeCreate(){ //before code will run
    this.$store.commit('initializeStore') //the commit will make initializeStore run or use the function
    console.log(this.$store.state.team) 
    console.log(this.$store.state.user) 

    if (this.$store.state.token){ //reference to the token 
        axios.defaults.headers.common['Authorization'] = 'Token ' + this.$store.state.token 
    } else {
        axios.defaults.headers.common['Authorization'] = ''
    }
    if (!this.$store.state.team.id){
      this.$router.push('/dashboard/add-team')
    }
  }
};
  
</script>

<style lang="scss">
@import '../node_modules/bulma';

.lds-dual-ring {
  display: inline-block;
  width: 800px;
  height: 80px;
}

.lds-dual-ring:after {
    content: " ";
    display: block;
    width: 64px;
    height: 64px;
    margin: 8px;
    border-radius: 50%;
    border: 6px solid #ccc;
    border-color: #ccc transparent #ccc transparent;
    animation: lds-dual-ring 1.2s linear infinite;
}

@keyframes lds-dual-ring {
    0% {
        transform: rotate(0deg);
    }
    100% {
        transform: rotate(360deg);
    }
}
.is-loading-bar {
    height: 0;
    overflow: hidden;
    -webkit-transition: all 0.3s;
    transition: all 0.3s;
    
    &.is-loading {
        height: 80px;
    }
}
</style>
