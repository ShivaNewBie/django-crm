<template>
    <div class="container">
        <div class="columns is-multiline">
            <div class="column is-12">
                <h1 class="title">Add Members </h1>
            </div>
         <form @submit.prevent='submitForm'> <!--to .prevent the default actions of html to be called -->
                    <div class="field">
                        <label>Email</label>
                        <div class="control">
                            <input type="email" name="username" class="input" v-model="username">
                        </div>
                    </div>

                    <div class="field">
                        <label>Password</label>
                        <div class="control">
                            <input type="password" name="password1" class="input" v-model="password1">
                        </div>
                    </div>

                    <div class="field">
                        <label>Repeat password</label>
                        <div class="control">
                            <input type="password" name="password2" class="input" v-model="password2">
                        </div>
                    </div>

                    <div class='notification is-danger' v-if='errors.length'> <!--Check if there are errors -->
                        <p v-for='error in errors' v-bind:key='error' >{{error}}</p>
                    </div>

                    <div class="field">
                        <div class="control">
                            <button class="button is-success">Submit</button>
                        </div>
                    </div>
                </form>
        </div>
    </div>
</template>

<script>
import axios from 'axios'

import {toast} from 'bulma-toast'

export default {
    name: 'AddMembers',
    data() {
        return{
        username: '',
        password1: '',
        password2: '',
        errors: []
        }
    },    
    methods: {
        async submitForm(){

            this.errors = []
            if (this.username === '') {
                this.errors.push('The username is missing')
            }

            if (this.password1 === ''){
                this.errors.push('The password is missing')

            }
            if (this.password2 === ''){
                this.errors.push('The password is missing')
            }

            if (!this.errors.length){ //if there are no errors
                this.$store.commit('setIsLoading',true)

                const emailData = {
                   'email':this.username

                }
                await axios
                    .post('api/v1/teams/add_member/', emailData) //sent data to backend
                    .then(response => {
                        toast({ 
                            message: 'Member created, please log in',
                            type: 'is-success',
                            dismissible: true,
                            pauseOnHover: true,
                            duration: 2000,
                            position: 'bottom-right'
                        })
                        this.$router.push({'name':'Team'}) //we will be redirected in this page when we are done
                    })
                    //always use catch to check if there are problems in server
                    .catch(error => {
                        if (error.response){
                            for(const property in error.response.data){
                                this.errors.push(`${property}: ${error.response.data[property]}`)
                            }
                        } else if (error.message){
                            this.errors.push('Something went wrong. Please try again')
                        }
                    })
                    this.$store.commit('setIsLoading',false)

            }
            // use this code to check if the function submitForm is working when clicking the submit buttonconsole.log('submitForm')
            // use this line to check if data is gathered after submitting = console.log(this.username)
            // check the number of errors console.log(this.errors.length) 
        }
    },
}
</script>