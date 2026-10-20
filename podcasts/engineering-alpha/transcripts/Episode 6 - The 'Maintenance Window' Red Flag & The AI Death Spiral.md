# Episode 6: The 'Maintenance Window' Red Flag & The AI Death Spiral

- **Playlist position:** 14
- **URL:** https://www.youtube.com/watch?v=OQBPTO5-jLk
- **Caption source:** auto-generated

---

[music] Two microphones, two opinions, [music] Two microphones, two opinions, one show. [music] This is Engineering Alpha in Private Equity, the Explainer episode with Paul Carner and Dave Mango. Thank you, Jay. Welcome everyone. We're back today with a special episode about a topic near and dear to Dave's heart and that is maintenance windows.

We we all know them. We're familiar with with uh from being on the consumer end of software when when a a software vendor has a maintenance window. We're going to talk about what that tells you about the organization and and what it what it means um in today's age. So yeah, I think you know the thing about maintenance windows is for our private equity listeners is they'll recognize this as something that is a holdover from let's call them legacy companies. I don't know what else how else you want to describe them.

We know private equity likes to buy companies that have been around for 20 years and we're going to fix them up and and all those kinds of things. And that's where we see maintenance windows, right? There's no brand new flashy AI startup that was started two weeks ago that's deploying things inside maintenance windows. Like that's just not a thing. And so for me, when I see maintenance windows at a company, I feel like that's a signal about the way that they develop software, the way that they release software.

And there's a lot of assumptions I make that I think are pretty grounded and pretty solid uh when I see those kinds of things. Gotcha. So what kinds of things might it tell you? Um what what you know I guess first of all like are there legitimate reasons to have maintenance windows? Um but kind of apart from those what what might it tell you about the organization?

Yeah, I think there's definitely times where maintenance windows are probably going to be necessary. Like that's a fact. Most of this stuff is, you know, you're a data scientist. Most of this stuff is around data, right? It's very hard to, you know, it's one thing to release software which says logic, you know, if this, then that or whatever, but like we're talking about data.

if you know an attribute of something is read like I need to be able to look up that attribute and if that attribute is there I can look it up and if it's not I can't and like if we're changing database schemas and it's in a different data store and what you know there's I don't want to get into it but like there can be definitely situations where that stuff could actually be necessary but like for the most part that's just not something we do anymore. I can add a column to a database table without taking downtime. That is not an issue. Uh so there are kinds of situations where you could need it. But most of our portfolio companies just not not in that space.

Uh but like the things that it does start to tell me about the way that they deploy is they probably don't have like a lot of automated tests. they probably don't have a lot of things built into the development life cycle that will take care of a lot of the concerns they have. And so I was working with a you know PE backed software company at one time and I was in their offices and they had this big meeting in the conference room and I sat in the meeting like I want to do. Uh and I they were they were calling it something like the uh release readiness meeting or something like that. And as part of the meeting, they went around the room to each of the department heads and they had a project manager.

I probably was running this because that's what you do in these kinds of organizations. And they asked each of the department heads, how do you feel about this release? Like what what are these people doing? you know, [laughter] and everybody around the room had to give a thumbs up or a thumbs down to how they felt about the release. [clears throat] I was just kind of ghast like at what I was watching because I've been doing this for decades and I don't even remember, you know, doing that.

Maybe we did back in back in the day, but you know, I live in California, you know, we're all super duper hippies here. like I love feelings like all that kind of stuff you know whatever fine um feelings are great at work like you know when I was an engineering leader I would talk to my engineers and be like how do you feel about how the team's doing like are things going well what are the things I should know about I I think feelings are great not for releasing software you know I was kind of like hey did the test pass yes green good ship. Did the test not pass? Okay, let's fix everything until the test pass. But like I don't care about your feelings about what you feel about the release cuz it doesn't mean anything.

It's nonsense. It's just it's garbage. Like it's your little window into what? Like it it doesn't do anything. And so like this idea that I'm talking about like did the test pass?

Did they not pass? Imagine this now with AI. Imagine I have AI write code and it's writing whatever who pick whichever metric you want 10 times as much code 100 times as much code like what am I going to do have 10 times as many meetings asking people how they feel about what they a like that's crazy like that's just not a thing that we can do and so um that kind of things where we have to hold everything up and like decide like as a group That's what I see when I see maintenance windows. I see like an organization that doesn't have their pipelines set up, that doesn't have their automation, that doesn't trust in their tests, and then they feel like getting some people to sit around and talk about it is an answer, but it's not. Yeah.

And it sounds like in other words what you're saying is it's I mean yes it's a bottleneck but it also is something about almost cultural um you know they're not they're not in the habit of of releasing software frequently and and you know as we've talked about in other episodes. [applause] Thank you. Thank you. [laughter] as we've talked about in other episodes um specifically uh with uh w with Nathan um and and and talking about the Dora research we know that that's what's necessary uh in part for uh good organizational outcomes, good business outcomes, right? We talked with Nathan about the fact that if you ship often then you're going to get better outcomes and maintenance windows is like literally the opposite of shipping often.

And you know, one of the things that I thought was like pretty good about, you know, what Nathan said that applies really directly here is he was like, if you release twice a year, you're guaranteed to have a failure. It's not, well, maybe this time everything will work out. Like, no, it's not. It's not going to work out. Like, you release twice a year.

And so like you know and what what happens is we release and then we have to release again because we find all the bugs and that's rework and rework is expensive. I don't want to pay my engineers to do the same work twice that's going to hit my ebida margins like guaranteed like I that's just crazy stuff and having AI do that faster and so we have to do more rework. What are we what are we gaining here now? I'm paying extra for the tokens and then I'm paying extra for the rework which is also the token. [laughter] It's like it's a death spiral.

I mean in some respects like it's just it's just you're going the wrong way. Speaking of AI, Dave, I was looking at our uh one of our favorite uh companies these days, Anthropic, their uh change log for Claude Code. And I noticed something really interesting. There's very detailed change logs. Their versions have two decimal points in them.

Uh and they release it looks like every day if not multiple times a day. Yeah. And that's what you're supposed to be doing, right? When we talked with Nathan about high performance software delivery organizations, one of the metrics was deployment frequency. And if you go and you dig into the research, which I'm probably the only geek who wants to do that, yeah, you'll see like the elite performers are releasing exactly what you just said daily or more likely multiple times a day.

And you talk about, you know, someone like Amazon, they're releasing thousands of times a day. And like it's just a competitive advantage that you can't you can't beat. And you know, like we talked about with Nathan, that's also increasing stability. And so, you know, a lot of times these private equity backed portfolio companies have been around for a while and they're like, either I can't release more often because my customers won't accept it, which I have heard in so many portfolio companies, it's not even funny. It's also wrong.

But, um, you know, there's also these concerns about compliance. I'm in a highly regulated industry. We're fintech or health tech, whatever. And like the things that people do to try to make it safer actually make it worse. And so there's research out there that proves that change advisory boards, most people in software know them as CABS, are inversely correlated with stability.

the thing that the change advisory boards are out there set out to do in cruise stability they are inversely correlated with which like is crazy and like you know what's the answer obviously is I think what a lot of people are wondering you know the answer is we have to have ways of satisfying those compliance requirements that don't involve having these meetings and slowing everything down and releasing less often and there's T I mean, I've been having these conversations all the way back to being an architect at Salesforce. Like, these aren't new conversations. We don't have to invent how to do this from whole cloth. Like, I teach portfolio companies how to do this every day. Um, but like those kinds of things that people are still carrying forward, especially ones that PE firms would buy, like they're not helping.

They're hurting. And we know we know how to do it better. And it's not necessarily a technology problem exclusively or even sounds like partially anymore. It's it's very much a cultural, you know, processes, all that. Um and and you're saying you've got um a lot of of uh sort of background and helping people kind of get over those get over the hump there.

Daily delivery is or daily shipping, whatever you want to call it, deployment is a culture. Like absolutely. And yes, can agents help us with this? And AI, of course, they can help. But like if you don't have the that practice, if that's not the way that your organization looks at problems, then like just rubbing some AI on it isn't going to fix it.

And you know, you and I have talked about this in the past, like these deployment companies and the stuff that the model vendors are spinning up and they don't solve the underlying problem of the way that people look at the work. And like if you don't solve that problem, the cultural aspects, the things that I'm working with CTO's on all the time, it doesn't the technology isn't doing anything. Technology has never been the hard part. And everybody that's listening that's ever been in any kind of a technology leadership position knows technology is never has never been the hard part. Like technology is fun.

Can it be challenging? Can it be interesting? Of course it can. But that's just never been the hard part because every day the computer's going to do the same thing. And people are just not like that.

And I wish that they were. Maybe. I think the world would be kind of boring. But um but yeah, that that's just not how it works. I think it's really interesting that you brought it back to this foundational stuff.

We've talked about this before with you know with with data um and you know kind of other aspects foundational aspects of the organization capabilities necessary to get AI to work. This is kind of another dimension or another angle uh on that. And uh you know I think uh if you can overcome it, if you can get the the right foundations in place, then you're in more of a a daily delivery uh kind of stance. Well, what does that what does that show you? Right?

We started by asking what is what does maintenance windows show you? What is what does the absence of that and and kind of more towards daily delivery show you? You're you're shipping often. You're good at it. You're getting customer feedback frequently.

U maybe that's your your your product kind of leading your growth. Yeah, that's your competitive advantage, right? That's a lot of people talk about PLG, product like growth. Like I want to be able to ship daily because I want to be able to run experiments. I want to be able to understand what my customers want and I want to be able to deliver that.

And if I'm have maintenance windows in order to figure that out, man, that is just going to kill your growth. And like what private equity firm doesn't want growth? like you show me one of them I because I don't I have never met any of them that don't want it. And then the other thing is, you know, something we touched on uh in terms of your IBIDA margins, right, is rework. Like if I'm doing activities that are guaranteed to cause rework, like it's it's just just slice that right out of of your IBA.

Like it's just silly. And we know how to do this stuff. And it's not about knowing, right? It's having that like culture in place. And this thing that we started with and it's you know feel like we're going to end with here is like these ideas of maintenance windows is an indicator of the culture of the software part of the organization.

It's not the technical stuff. Yeah. Okay. Fine. Like like we we can figure out how to do those things.

But that's what the marker is. And like I'm not saying it's easy. Clearly I work with companies on this every day. if it was easy, they wouldn't even talk to me. Um, but like it is necessary if you actually want to be out there and be competitive.

Fascinating. Great stuff, Dave. All right, catch you all next time. Cheers.
