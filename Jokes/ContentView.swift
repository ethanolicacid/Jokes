//
//  ContentView.swift
//  Jokes
//
//  Created by Ethan Lim on 2/7/22.
//

import SwiftUI

struct ContentView: View {

    var jokesList = [
    Joke(setup: "The calendar is about to die.", punchline: "Its days are numbered.", explainer: "The days on the calendar have numbers indicating what day it is."),
    Joke(setup: "I only seem to get sick on weekdays.", punchline: "I think I have a weekend immune system.", explainer: "Weakened sounds like weekend."),
    Joke(setup: "Which days of the week are strongest?", punchline: "Saturdays and Sundays, the other days are weekdays.", explainer: "Week sounds like weak, so weekdays sounds like weak days."),
    Joke(setup: "It's easy to deter women from eating laundry pods.", punchline: "But it's harder to deter gents", explainer: "Deter gents looks like the word detergents, gents mean male people, so deter gents means stop males."),
    ]
    @State var showPunchline = false
    @State var showExplainer = false
    @State var currentJoke = 0
    var body: some View {
        VStack{
            Text(jokesList[0].setup)
                .font(.title2)
                .padding()
            
            HStack{}
            Button{
                print("Button tapped")
                showPunchline = true
            } label:{
                Text("Then?")
                    .font(.title3)
                    .foregroundColor(.white)
                    .padding()
                    .background(Color(red: 0.2, green: 0.4, blue: 0.9))
                    .cornerRadius(10)
                    .padding(10)
            }
            .padding()
            
            Button{
                print("Button tapped")
                showPunchline = true
            } label:{
                Text("Then?")
                    .font(.title3)
                    .foregroundColor(.white)
                    .padding()
                    .background(Color(red: 0.2, green: 0.4, blue: 0.9))
                    .cornerRadius(10)
                    .padding(10)
            }
            .padding()
            
            if showPunchline{
                Text(jokesList[currentJoke].punchline)
                    .padding()
                Text("Next joke")
                    .foregroundColor(Color(red: 0.4, green: 0.4, blue: 0.4))
                
                Button{
                    print("Button tapped")
                    showPunchline = true
                } label:{
                    Text("Huh?")
                        .font(.title3)
                        .foregroundColor(.white)
                        .padding()
                        .background(Color(red: 0.2, green: 0.4, blue: 0.9))
                        .cornerRadius(10)
                        .padding(10)
                }
                .padding()
                
            }
        }
    }
}

struct ContentView_Previews: PreviewProvider {
    static var previews: some View {
        ContentView()
    }
}
